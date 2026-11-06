from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.db.models import Q, Count, Avg
from django.contrib import messages
from .models import Category, Creation, PlaytestReview, DesignChallenge, ChallengeSubmission
from .forms import CreationForm, PlaytestReviewForm
import random

def home(request):
    query = request.GET.get('q', '').strip()
    category_slug = request.GET.get('category', '')
    creation_type = request.GET.get('type', '')
    difficulty = request.GET.get('difficulty', '')
    sort_by = request.GET.get('sort', 'sparks')

    creations = Creation.objects.select_related('category').all()

    if query:
        creations = creations.filter(
            Q(title__icontains=query) |
            Q(tagline__icontains=query) |
            Q(description__icontains=query) |
            Q(novelty_factor__icontains=query) |
            Q(materials_needed__icontains=query) |
            Q(stem_fields__icontains=query)
        )

    if category_slug:
        creations = creations.filter(category__slug=category_slug)

    if creation_type:
        creations = creations.filter(creation_type=creation_type)

    if difficulty:
        creations = creations.filter(difficulty=difficulty)

    if sort_by == 'newest':
        creations = creations.order_by('-created_at')
    elif sort_by == 'rating':
        creations = creations.order_by('-sparks_count')
    else: # default sparks
        creations = creations.order_by('-sparks_count', '-created_at')

    categories = Category.objects.annotate(creation_count=Count('creations'))
    featured_creations = Creation.objects.filter(is_featured=True)[:4]
    active_challenges = DesignChallenge.objects.filter(is_active=True)[:2]

    stats = {
        'total_creations': Creation.objects.count(),
        'total_sparks': sum(c.sparks_count for c in Creation.objects.all()),
        'total_reviews': PlaytestReview.objects.count(),
        'total_prototypes': Creation.objects.exclude(prototype_type='NONE').count(),
    }

    context = {
        'creations': creations,
        'categories': categories,
        'featured_creations': featured_creations,
        'active_challenges': active_challenges,
        'stats': stats,
        'current_category': category_slug,
        'current_type': creation_type,
        'current_difficulty': difficulty,
        'current_sort': sort_by,
        'query': query,
    }
    return render(request, 'creations/home.html', context)


def creation_detail(request, slug):
    creation = get_object_or_404(Creation.objects.select_related('category'), slug=slug)
    
    # Track view
    Creation.objects.filter(pk=creation.pk).update(views_count=creation.views_count + 1)
    creation.refresh_from_db()

    review_form = PlaytestReviewForm()

    if request.method == 'POST':
        review_form = PlaytestReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.creation = creation
            review.save()
            messages.success(request, "Your playtest review has been recorded! Thank you for helping the inventor iterate.")
            return redirect('creations:detail', slug=creation.slug)

    reviews = creation.reviews.all()
    related_creations = Creation.objects.filter(category=creation.category).exclude(pk=creation.pk)[:3]

    context = {
        'creation': creation,
        'reviews': reviews,
        'review_form': review_form,
        'related_creations': related_creations,
    }
    return render(request, 'creations/detail.html', context)


def creation_create(request):
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            creation = form.save()
            messages.success(request, f"'{creation.title}' has been forged! Your blueprint is live.")
            return redirect('creations:detail', slug=creation.slug)
    else:
        # Check if pre-filled from spark generator
        initial = {}
        if 'spark_title' in request.GET:
            initial['title'] = request.GET.get('spark_title')
        if 'spark_tagline' in request.GET:
            initial['tagline'] = request.GET.get('spark_tagline')
        if 'spark_type' in request.GET:
            initial['creation_type'] = request.GET.get('spark_type')
        if 'spark_novelty' in request.GET:
            initial['novelty_factor'] = request.GET.get('spark_novelty')
        if 'spark_materials' in request.GET:
            initial['materials_needed'] = request.GET.get('spark_materials')
        if 'spark_age_min' in request.GET:
            initial['target_age_min'] = request.GET.get('spark_age_min')
        if 'spark_stem' in request.GET:
            initial['stem_fields'] = request.GET.get('spark_stem')
        
        form = CreationForm(initial=initial)

    return render(request, 'creations/create.html', {'form': form})


def spark_creation(request, slug):
    creation = get_object_or_404(Creation, slug=slug)
    # Toggle spark in session
    sparked_creations = request.session.get('sparked_creations', [])
    
    if creation.pk in sparked_creations:
        creation.sparks_count = max(0, creation.sparks_count - 1)
        sparked_creations.remove(creation.pk)
        sparked = False
    else:
        creation.sparks_count += 1
        sparked_creations.append(creation.pk)
        sparked = True
    
    creation.save()
    request.session['sparked_creations'] = sparked_creations

    if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
        return JsonResponse({
            'sparks_count': creation.sparks_count,
            'sparked': sparked
        })
    
    return redirect('creations:detail', slug=slug)


def playlab_hub(request):
    playable_creations = Creation.objects.exclude(prototype_type='NONE')
    context = {
        'playable_creations': playable_creations
    }
    return render(request, 'creations/playlab_hub.html', context)


def playlab_simulator(request, prototype_type):
    # Supported: marble-run, chroma-tiles, kinetic-gears
    template_name = 'creations/prototypes/marble_run.html'
    title = "CogCraft Kinetic Contraption Sandbox"
    slug_proto = 'MARBLE_RUN'

    if prototype_type == 'chroma-tiles':
        template_name = 'creations/prototypes/chroma_tiles.html'
        title = "ChromaTiles Tactical Light-Grid Game"
        slug_proto = 'CHROMA_TILES'
    elif prototype_type == 'kinetic-gears':
        template_name = 'creations/prototypes/kinetic_gears.html'
        title = "GearSmith Kinematic Automaton Lab"
        slug_proto = 'KINETIC_GEARS'

    matched_creation = Creation.objects.filter(prototype_type=slug_proto).first()

    context = {
        'prototype_type': prototype_type,
        'title': title,
        'matched_creation': matched_creation,
    }
    return render(request, template_name, context)


def spark_generator(request):
    """Creative Ideation Machine for novel toys & games"""
    # Preset creative combinatorial engines
    AUDIENCES = [
        "Curious 6-8 year olds who love dismantling gadgets",
        "Multi-generational families playing on game night",
        "Adult puzzle enthusiasts seeking extreme spatial challenges",
        "Sensory-seeking toddlers and neurodivergent kids",
        "Classroom STEM students learning physics in groups",
        "Solo tabletop tacticians looking for 15-minute deep puzzles"
    ]
    
    MECHANICS = [
        "Repulsive neodymium magnet levitation",
        "Gravitational marble acceleration with counterweight pendulums",
        "Prismatic optical light beam reflection and refraction",
        "Modular interlocking gears with eccentric cam linkages",
        "Bistable compliant spring flexures and snap-action origami",
        "Fluidic hydraulic pressure channels with colored air-water vials",
        "Hidden blind-bidding combined with rotating spatial labyrinth boards"
    ]

    MATERIALS = [
        "Recycled corrugated cardboard & bamboo skewers",
        "Precision laser-cut birch plywood and brass hardware",
        "Conductive graphite pencil traces & LED coin-cell circuits",
        "3D printed flexible TPU polymers and carbon fiber rods",
        "Smooth river stones, magnetic silicone putty & acrylic domes",
        "Cardstock origami folds paired with elastic polymer bands"
    ]

    THEMES = [
        "Deep-sea abyss bioluminescent exploration",
        "Zero-gravity orbital repair station",
        "Time-traveling clockwork subterranean city",
        "Mythological forest where trees whisper harmonic frequencies",
        "Microscopic particle accelerator tournament",
        "Wind-powered desert nomadic convoy race"
    ]

    context = {
        'audiences': AUDIENCES,
        'mechanics': MECHANICS,
        'materials': MATERIALS,
        'themes': THEMES,
    }
    return render(request, 'creations/spark_generator.html', context)


def challenges_list(request):
    challenges = DesignChallenge.objects.annotate(entry_count=Count('submissions')).order_by('-created_at')
    return render(request, 'creations/challenges.html', {'challenges': challenges})


def challenge_detail(request, slug):
    challenge = get_object_or_404(DesignChallenge, slug=slug)
    submissions = ChallengeSubmission.objects.filter(challenge=challenge).select_related('creation')
    user_creations = Creation.objects.all()

    if request.method == 'POST':
        creation_id = request.POST.get('creation_id')
        if creation_id:
            creation = get_object_or_404(Creation, pk=creation_id)
            if not ChallengeSubmission.objects.filter(challenge=challenge, creation=creation).exists():
                ChallengeSubmission.objects.create(challenge=challenge, creation=creation)
                messages.success(request, f"'{creation.title}' submitted to '{challenge.title}'!")
            else:
                messages.info(request, "This creation is already submitted to this challenge.")
            return redirect('creations:challenge_detail', slug=slug)

    context = {
        'challenge': challenge,
        'submissions': submissions,
        'user_creations': user_creations,
    }
    return render(request, 'creations/challenge_detail.html', context)


def print_blueprint(request, slug):
    creation = get_object_or_404(Creation, slug=slug)
    return render(request, 'creations/print_blueprint.html', {'creation': creation})

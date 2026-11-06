from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import uuid

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, default='puzzle-piece', help_text="FontAwesome or Lucide icon name")
    accent_color = models.CharField(max_length=20, default='#6366f1')

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Creation(models.Model):
    TYPE_CHOICES = [
        ('TOY', 'Unique Toy Concept'),
        ('GAME', 'Original Board / Tabletop Game'),
        ('HYBRID', 'Interactive / Digital-Physical Hybrid'),
    ]

    DIFFICULTY_CHOICES = [
        ('EASY', 'Beginner / Family Friendly'),
        ('MEDIUM', 'Intermediate / Hobbyist'),
        ('ADVANCED', 'Advanced / Maker Level'),
        ('MASTER', 'Master / Engineering Prototype'),
    ]

    PROTOTYPE_CHOICES = [
        ('NONE', 'Blueprint Only'),
        ('MARBLE_RUN', 'Kinetic Contraption Sandbox (Interactive)'),
        ('CHROMA_TILES', 'ChromaTiles Tactical Game (Playable)'),
        ('KINETIC_GEARS', 'Gear Motion Toy Simulator (Interactive)'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    creation_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='TOY')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='creations')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='creations')
    creator_name = models.CharField(max_length=100, default='ToySmith Studio')
    
    tagline = models.CharField(max_length=250, help_text="A catchy one-sentence summary of the toy or game.")
    description = models.TextField(help_text="In-depth conceptual overview and how it works.")
    novelty_factor = models.TextField(help_text="What makes this toy or game fundamentally unique and never seen before?")
    
    target_age_min = models.PositiveIntegerField(default=6)
    target_age_max = models.PositiveIntegerField(default=99)
    player_count_min = models.PositiveIntegerField(default=1)
    player_count_max = models.PositiveIntegerField(default=4)
    play_time_minutes = models.PositiveIntegerField(default=20, help_text="Estimated play session or build duration in minutes.")
    
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='MEDIUM')
    
    materials_needed = models.TextField(help_text="Comma-separated or line-separated list of required parts/materials.")
    tools_required = models.TextField(blank=True, help_text="Tools needed to assemble or craft (e.g., 3D printer, scissors, glue).")
    rules_or_instructions = models.TextField(help_text="Rules of play or step-by-step assembly instructions.")
    safety_advisories = models.TextField(blank=True, default="Contains small components. Not suitable for children under 3 years.")
    stem_fields = models.CharField(max_length=200, default="Physics, Mechanics, Spatial Logic", help_text="Relevant STEM disciplines.")
    
    prototype_type = models.CharField(max_length=30, choices=PROTOTYPE_CHOICES, default='NONE')
    banner_color = models.CharField(max_length=50, default='from-indigo-600 to-purple-600')
    badge_tag = models.CharField(max_length=50, blank=True, default='Featured Innovation')
    
    sparks_count = models.PositiveIntegerField(default=0)
    views_count = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-sparks_count', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title) or 'creation'
            unique_slug = base_slug
            counter = 1
            while Creation.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def average_rating(self):
        reviews = self.reviews.all()
        if not reviews:
            return 5.0
        return round(sum(r.rating_overall for r in reviews) / len(reviews), 1)

    def materials_list(self):
        return [m.strip() for m in self.materials_needed.split('\n') if m.strip()]

    def __str__(self):
        return f"{self.title} ({self.get_creation_type_display()})"


class PlaytestReview(models.Model):
    creation = models.ForeignKey(Creation, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    rating_overall = models.PositiveSmallIntegerField(default=5)
    rating_fun = models.PositiveSmallIntegerField(default=5)
    rating_originality = models.PositiveSmallIntegerField(default=5)
    rating_durability = models.PositiveSmallIntegerField(default=5)
    rating_stem_value = models.PositiveSmallIntegerField(default=5)
    comment = models.TextField()
    maker_mod_idea = models.TextField(blank=True, help_text="Idea for a DIY hack or gameplay modification")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Review by {self.reviewer_name} for {self.creation.title}"


class DesignChallenge(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    theme = models.CharField(max_length=150)
    description = models.TextField()
    constraints = models.TextField(help_text="Design rules and required constraints")
    reward_title = models.CharField(max_length=100, default="Master Toymaker Badge")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ChallengeSubmission(models.Model):
    challenge = models.ForeignKey(DesignChallenge, on_delete=models.CASCADE, related_name='submissions')
    creation = models.ForeignKey(Creation, on_delete=models.CASCADE, related_name='challenge_entries')
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('challenge', 'creation')

    def __str__(self):
        return f"{self.creation.title} in {self.challenge.title}"

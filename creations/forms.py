from django import forms
from .models import Creation, PlaytestReview, DesignChallenge

class CreationForm(forms.ModelForm):
    class Meta:
        model = Creation
        fields = [
            'title',
            'tagline',
            'creation_type',
            'category',
            'creator_name',
            'novelty_factor',
            'description',
            'target_age_min',
            'target_age_max',
            'player_count_min',
            'player_count_max',
            'play_time_minutes',
            'difficulty',
            'materials_needed',
            'tools_required',
            'rules_or_instructions',
            'safety_advisories',
            'stem_fields',
            'prototype_type',
            'banner_color',
            'badge_tag',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., GyroGlide: Magnetic Kinetic Levitator'}),
            'tagline': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Catchy 1-sentence hook...'}),
            'creation_type': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'creator_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your inventor alias or team name'}),
            'novelty_factor': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 3, 'placeholder': 'What makes this toy/game fundamentally original? E.g., uses magnetic repulsive fluid... '}),
            'description': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 5, 'placeholder': 'Full concept, lore, how it plays or functions...'}),
            'target_age_min': forms.NumberInput(attrs={'class': 'form-input', 'min': 3, 'max': 99}),
            'target_age_max': forms.NumberInput(attrs={'class': 'form-input', 'min': 3, 'max': 99}),
            'player_count_min': forms.NumberInput(attrs={'class': 'form-input', 'min': 1, 'max': 20}),
            'player_count_max': forms.NumberInput(attrs={'class': 'form-input', 'min': 1, 'max': 50}),
            'play_time_minutes': forms.NumberInput(attrs={'class': 'form-input', 'min': 5, 'max': 360}),
            'difficulty': forms.Select(attrs={'class': 'form-select'}),
            'materials_needed': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4, 'placeholder': 'List materials (one per line): e.g., \n- 8x Neodymium magnets\n- 4mm Acrylic sheet\n- 12x Steel ball bearings'}),
            'tools_required': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., 3D Printer, Hot Glue Gun, Hex Screwdriver'}),
            'rules_or_instructions': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 6, 'placeholder': 'Rules of play or step-by-step DIY build guide...'}),
            'safety_advisories': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., Strong magnetic field hazard; not for children under 5'}),
            'stem_fields': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., Electromagnetism, Angular Momentum, Aerodynamics'}),
            'prototype_type': forms.Select(attrs={'class': 'form-select'}),
            'banner_color': forms.Select(attrs={'class': 'form-select'}, choices=[
                ('from-indigo-600 to-purple-600', 'Indigo Purple Nebula'),
                ('from-amber-500 to-rose-600', 'Solar Flare Amber'),
                ('from-emerald-500 to-teal-700', 'Emerald Matrix'),
                ('from-cyan-500 to-blue-600', 'Oceanic Cyan Pulse'),
                ('from-fuchsia-600 to-pink-600', 'Neon Cyber Pink'),
                ('from-violet-600 to-indigo-900', 'Deep Space Void'),
            ]),
            'badge_tag': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., STEM Certified, Kickstarter Ready'}),
        }


class PlaytestReviewForm(forms.ModelForm):
    class Meta:
        model = PlaytestReview
        fields = [
            'reviewer_name',
            'rating_overall',
            'rating_fun',
            'rating_originality',
            'rating_durability',
            'rating_stem_value',
            'comment',
            'maker_mod_idea',
        ]
        widgets = {
            'reviewer_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your name or playtester handle'}),
            'rating_overall': forms.Select(attrs={'class': 'form-select'}, choices=[(i, f"{i} Stars") for i in range(5, 0, -1)]),
            'rating_fun': forms.Select(attrs={'class': 'form-select'}, choices=[(i, f"{i}/5 Fun Factor") for i in range(5, 0, -1)]),
            'rating_originality': forms.Select(attrs={'class': 'form-select'}, choices=[(i, f"{i}/5 Innovation") for i in range(5, 0, -1)]),
            'rating_durability': forms.Select(attrs={'class': 'form-select'}, choices=[(i, f"{i}/5 Durability/Rules") for i in range(5, 0, -1)]),
            'rating_stem_value': forms.Select(attrs={'class': 'form-select'}, choices=[(i, f"{i}/5 STEM Educational") for i in range(5, 0, -1)]),
            'comment': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4, 'placeholder': 'Share detailed feedback on gameplay balance, physical feel, and kids/adult reaction...'}),
            'maker_mod_idea': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 2, 'placeholder': 'Optional hack or expansion suggestion...'}),
        }

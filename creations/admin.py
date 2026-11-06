from django.contrib import admin
from .models import Category, Creation, PlaytestReview, DesignChallenge, ChallengeSubmission

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'icon', 'accent_color')
    prepopulated_fields = {'slug': ('name',)}

class PlaytestReviewInline(admin.TabularInline):
    model = PlaytestReview
    extra = 1

@admin.register(Creation)
class CreationAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_type', 'category', 'difficulty', 'sparks_count', 'is_featured', 'created_at')
    list_filter = ('creation_type', 'category', 'difficulty', 'is_featured')
    search_fields = ('title', 'tagline', 'description', 'materials_needed')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PlaytestReviewInline]

@admin.register(PlaytestReview)
class PlaytestReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer_name', 'creation', 'rating_overall', 'created_at')
    list_filter = ('rating_overall', 'created_at')
    search_fields = ('reviewer_name', 'comment', 'creation__title')

@admin.register(DesignChallenge)
class DesignChallengeAdmin(admin.ModelAdmin):
    list_display = ('title', 'theme', 'reward_title', 'is_active', 'created_at')
    list_filter = ('is_active',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(ChallengeSubmission)
class ChallengeSubmissionAdmin(admin.ModelAdmin):
    list_display = ('challenge', 'creation', 'submitted_at')
    list_filter = ('challenge',)

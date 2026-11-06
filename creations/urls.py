from django.urls import path
from . import views

app_name = 'creations'

urlpatterns = [
    path('', views.home, name='home'),
    path('creations/new/', views.creation_create, name='create'),
    path('creations/<slug:slug>/', views.creation_detail, name='detail'),
    path('creations/<slug:slug>/spark/', views.spark_creation, name='spark'),
    path('creations/<slug:slug>/print/', views.print_blueprint, name='print_blueprint'),
    
    # PlayLab (Interactive in-browser playable prototypes)
    path('playlab/', views.playlab_hub, name='playlab_hub'),
    path('playlab/<str:prototype_type>/', views.playlab_simulator, name='playlab_simulator'),
    
    # Spark Ideation Hub & Challenges
    path('spark-engine/', views.spark_generator, name='spark_generator'),
    path('challenges/', views.challenges_list, name='challenges_list'),
    path('challenges/<slug:slug>/', views.challenge_detail, name='challenge_detail'),
]

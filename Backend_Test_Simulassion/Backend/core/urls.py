from django.urls import path
from .views import create_short_url, get_stats, redirect_url

urlpatterns = [
    path('', create_short_url),
    path('<str:shortcode>/', get_stats),
    path('go/<str:shortcode>/', redirect_url),
]
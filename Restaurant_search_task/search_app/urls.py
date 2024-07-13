from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('search/', views.search_view, name='search_results'),
    # Add other paths as needed
]

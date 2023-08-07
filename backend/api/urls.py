"""This function is used for defining URL patterns in your Django project. 
It is a way to map specific URL paths to views or other URL patterns. """
from django.urls import path, include

from . import views
# from . views import api_home

urlpatterns = [
    path("", views.api_home) #localhost:8000/home
    # path('api/', include('api.urls')),
]

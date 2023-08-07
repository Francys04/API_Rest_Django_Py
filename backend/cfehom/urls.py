"""cfehom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""This line imports the admin module from django.contrib, 
which provides the Django admin interface for managing models and data in the application."""
from django.contrib import admin
"""This line imports the path function from django.urls, which is used to define URL patterns for 
routing requests, and the include function, which is used to include other URL patterns from different modules."""
from django.urls import path, include

"""This line defines the list of URL patterns for your Django project. 
It's a list of route patterns that map to specific views in your application."""
urlpatterns = [
    path('admin/', admin.site.urls), # When a user visits /admin/ in the browser, they will be directed to the admin interface for managing models and data.
    path('api/', include('api.urls')), # It effectively delegates further URL routing to the 'api.urls' module.
    path('api/products', include('products.urls')), # This pattern maps the URL 'api/products' to the included URLs from the 'products.urls' module. 
]

# localhost:8000/api/

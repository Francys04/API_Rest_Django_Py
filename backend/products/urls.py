from django.urls import path

from . import views

# declare the path to access
# url is an int
urlspatterns = [
    path('<int:pk>/', views.product_detail_view)
]
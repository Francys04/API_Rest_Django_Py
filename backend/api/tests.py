"""Provides methods for working with JSON (JavaScript Object Notation) data."""
import json
"""This line imports the TestCase class and RequestFactory class from the django.test module. 
The TestCase class is used for writing tests for Django applications, and the """
from django.test import TestCase, RequestFactory
"""It provides predefined HTTP status codes that can be used in Django REST framework views and tests."""
from rest_framework import status
"""The APIRequestFactory class is a test utility provided by Django REST framework for creating mock API requests."""
from rest_framework.test import APIRequestFactory
"""This function is presumably a view function in a Django application that handles API requests."""
from .views import api_home
"""This suggests that the code is related to a Django application with a Product model."""
from products.models import Product
"""This is likely the serializer used to convert Product model instances to and from JSON data."""
from products.serializers import ProductSerializer

class TestApiHomeView(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_valid_get_request(self):
        # Create a sample product
        product = Product.objects.create(title='Test Product', price=10.99)
        # Create a GET request
        request = self.factory.get('/api/home/')
        response = api_home(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['id'], product.id)
        self.assertEqual(response.data[0]['title'], product.title)
        self.assertEqual(response.data[0]['price'], str(product.price))

    def test_invalid_get_request(self):
        # Create an invalid GET request
        request = self.factory.get('/api/home/')
        response = api_home(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'invalid': 'not good data'})

    def test_valid_get_request_with_serializer(self):
        # Create a sample product
        product = Product.objects.create(title='Test Product', price=10.99)
        # Create a GET request with a valid serializer
        request = self.factory.get('/api/home/')
        serializer = ProductSerializer(instance=product)
        response = api_home(request, data=serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['id'], product.id)
        self.assertEqual(response.data[0]['title'], product.title)
        self.assertEqual(response.data[0]['price'], str(product.price))

    def test_invalid_get_request_with_serializer(self):
        # Create an invalid GET request with an invalid serializer
        request = self.factory.get('/api/home/')
        serializer = ProductSerializer(data={'invalid': 'data'})
        response = api_home(request, data=serializer.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'invalid': 'not good data'})

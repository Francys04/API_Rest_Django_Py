
## Django-Rest-API-Framework
This repository demonstrates the implementation of a Django application that serves as a RESTful API for managing product information. The application is built using the Django web framework and the Django REST framework, making it easy to create, retrieve, update, and delete product data through HTTP requests.

### Table of Contents
- Introduction
- Getting Started
- Requirements
- Setup
- API Endpoints
- Models
- Serializers
- URL Patterns
- Views
- Testing

1. Introduction
- The Django RESTful API Example showcases the use of the Django framework and the Django REST framework to create a simple API for managing product data. It includes functionalities such as fetching product details, creating new products, and handling API requests.

2. Getting Started
#### Requirements
- Python (3.6+)
- Django (3.0+)
- Django REST framework (3.12+)
3. Setup
- Clone the repository:
git clone https://github.com/Francys04/API_Rest_Django_Py
- Install the required dependencies:
`pip install -r requirements.txt`
- Apply migrations to create the database schema:
`python manage.py migrate`
- Start the Django development server:
`python manage.py runserver`
- The API will be accessible at http://localhost:8000/api/.

4. API Endpoints
The following API endpoints are available:

- GET /api/products/1/: Retrieves detailed information about a specific product with ID 1.
5. Models
- The application includes a Product model with the following fields:

`title (CharField)`: The title of the product.
`content (TextField, optional)`: Additional content describing the product.
`price (DecimalField)`: The price of the product.

6. Serializers
- A ProductSerializer is provided to convert Product model instances to and from JSON format. The serializer also includes calculated properties such as sale_price and get_discount.

7. URL Patterns
- The URL patterns are defined to route requests to the appropriate views. The following URL pattern is included:

- GET /api/products/<int:pk>/: Retrieves detailed information about a specific product based on the provided primary key (PK).
8. Views
- The views in this application are implemented using Django REST framework's generics. The ProductDetailAPIView class handles the retrieval of detailed product information based on the provided primary key (PK).

9. Testing
- Unit tests have been implemented to ensure the functionality of the API and views. To run the tests, use the following command:
`python manage.py test`
- The tests cover scenarios such as valid and invalid requests, serializer behavior, and API responses.
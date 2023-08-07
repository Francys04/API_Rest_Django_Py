"""JSON is often used to serialize data for communication between a client and a server."""
import json
"""This line imports the JsonResponse class from the django.http module. 
JsonResponse is a Django class that allows you to create HTTP responses with JSON-encoded content. 
It's often used to return JSON responses from views."""
from django.http import JsonResponse
"""The Response class is provided by the Django REST framework and is an enhanced 
version of Django's HttpResponse that is tailored for working with RESTful APIs."""
from rest_framework.response import Response
"""The api_view decorator is used to define function-based views that are compatible with the 
Django REST framework. It provides various features and enhancements for building API views."""
from rest_framework.decorators import api_view

# # create test view of django frame
# def api_home(request, *args, **kwargs):
#     # request -> HTTPRequest -> Django
#     # request .body
#     # print(dir(request))
#     body = request.body  #byte string of JSON data
#     data = {}
#     try:
#         data = json.loads(body) # string od JSON data -> Py Dict
#     except:
#         pass
#     print(data)
#     data['headers'] = request.headers #request.META ->
#     data['content_type'] = request.content_type
#     return JsonResponse({"message": "hi, this is your django"})
# # Create your views here.




# create a api response with migrations and migrate cmd and python shell cmd
# django model instance to dict

from django.forms.models import model_to_dict
from products.models import Product
# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data={}
    # if exist data
    # if model_data:
    #     data['id'] = model_data.id
    #     data['title'] = model_data.title
    #     data["content"] = model_data.content
    #     data['price'] = model_data.price
    #     # model instance (model_data)
    #     # turn a Py dict
    #     # return JSON to my client
    
    
    
    # model_to_dict
    # if model_data:
    #     data = model_to_dict(model_data)
    # return JsonResponse(data)
    
    
    # model serialisation
from products.serializers import ProductSerializer    

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
        print(serializer.data)
        return Response(serializer.data)
    return Response({'invalid':'not good data'}, status=400)
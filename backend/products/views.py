# Rest Frame Generics
from rest_framework import generics


from .models import Product
from .serializers import ProductSerializer




# decalre class od APIView
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # look_up_field = 'pk'
    
    # Product.object.get(pk='abc')
    
product_detail_view = ProductDetailAPIView.as_view()
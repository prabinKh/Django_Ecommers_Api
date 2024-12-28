from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import *
from .serialization import *
from rest_framework.response import Response
from rest_framework.decorators import action

from .product_recomended import get_similar_products
class Laptopview(viewsets.ModelViewSet):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer


class Tagview(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class Reviewview(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    


# class ProductView(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     #  .order_by("?")[:40]
#     serializer_class = ProductSerializer

#     def recommendations(self, request,pk = None):
#         similar_product = get_similar_products(pk,10)
#         serializer = ProductSerializer(similar_product,many = True)
#         return Response(serializer.data)
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("?")[:40]
    serializer_class = ProductSerializer
    

    @action(detail=True, methods=['get'])
    def recommendations(self, request, pk=None):
        similar_products = get_similar_products(pk, 10)
        serializer = ProductSerializer(similar_products, many=True)
        print(serializer.data)
        return Response(serializer.data)
    


# class ProductDetailApi(viewsets.ModelViewSet):
#     queryset = Product.objects.get(id = id)

#     serializer_class = ProductSerializer


def productfrontend(request):
    return render(request,"product.html")
def productdetailfrontend(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "productdetail.html", {"product": product})
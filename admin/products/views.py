from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product, User
from .serializers import ProductSerializer
from .producer import publish

import random



# REST API C.R.U.D METHODS(5)
## Product
class ProductViewSet(viewsets.ViewSet):
    def list(self, request): # /api/products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True) # should return an array
        return Response(serializer.data)

    def create(self, request): # /api/products
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created', serializer.data) # when we add new product, publish it(data) for consumption
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_updated', serializer.data) # Event we want to send
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        product.delete()
        publish('product_deleted', pk) # Event we want to send
        return Response(status=status.HTTP_204_NO_CONTENT)

## User
class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        # Get a random user
        user = random.choice(users)
        return Response({
            'id': user.id
        })
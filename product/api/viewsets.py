from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from product.api.serializers import ProductSerializer, CategorySerializer
from product.models import Product, Category

class ProductViewSet(ModelViewSet):
    serializer_class       = ProductSerializer
    search_fields          = ["id"]
    filter_backends        = (SearchFilter, OrderingFilter)
    ordering               = ('id')

    def get_queryset(self):
        return Product.objects.all()

class CategoryViewSet(ModelViewSet):
    serializer_class       = CategorySerializer
    search_fields          = ["id"]
    filter_backends        = (SearchFilter, OrderingFilter)
    ordering               = ('id')

    def get_queryset(self):
        return Category.objects.all()
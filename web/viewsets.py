from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Product, SubCategories, Categories
from .serializers import ProductSerializer, CategorySerializer, SubCategorySerializer


class ProductViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_fields = ('subcategory', 'subcategory__category',)


class SubCategoryViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         GenericViewSet):
    queryset = SubCategories.objects.all()
    serializer_class = SubCategorySerializer
    filter_fields = ('category',)


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

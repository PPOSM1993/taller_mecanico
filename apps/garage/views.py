from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .models import Category, Brand, Car
from .serializers import CategorySerializer, BrandSerializer, CarSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import (LimitOffsetPagination,PageNumberPagination)
from rest_framework import status


# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.order_by('pk')
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

    pagination_class = PageNumberPagination
    pagination_class.page_size = 5
    pagination_class.page_query_param = 'pagenum'
    pagination_class.page_size_query_param ='size'
    pagination_class.max_page_size = 10

    def get_permissions(self):
        self.permission_classes = [AllowAny]

        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
    
    def list(self, request):
        category_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(category_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):        
        #crea la categoria de el taller mecanico
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Categoria creada correctamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            category_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if category_serializer.is_valid():
                category_serializer.save()
            return Response({"message":"Categoria eliminada correctamente"}, status=status.HTTP_200_OK)
        return Response({"message":"Categoria no encontrada en la base de datos"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        category = self.get_queryset().filter(id=pk).first()
        if category:
            category.state = False
            category.save()
            return Response({"message":"Categoria eliminada correctamente"}, status=status.HTTP_200_OK)
        return Response({"message":"Categoria no encontrada en la base de datos"}, status=status.HTTP_400_BAD_REQUEST)


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.order_by('pk')
    serializer_class = BrandSerializer
    permission_classes = [AllowAny]

    pagination_class = PageNumberPagination
    pagination_class.page_size = 5
    pagination_class.page_query_param = 'pagenum'
    pagination_class.page_size_query_param ='size'
    pagination_class.max_page_size = 10

    def get_permissions(self):
        self.permission_classes = [AllowAny]

        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]

        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def list(self, request):
        brand_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(brand_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):        
        #crea la categoria de el taller mecanico
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Categoria creada correctamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            brand_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if brand_serializer.is_valid():
                brand_serializer.save()
            return Response({"message":"Categoria eliminada correctamente"}, status=status.HTTP_200_OK)
        return Response({"message":"Categoria no encontrada en la base de datos"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        brand = self.get_queryset().filter(id=pk).first()
        if brand:
            brand.state = False
            brand.save()
            return Response({"message":"Categoria eliminada correctamente"}, status=status.HTTP_200_OK)
        return Response({"message":"Categoria no encontrada en la base de datos"}, status=status.HTTP_400_BAD_REQUEST)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.order_by('pk')
    serializer_class = CarSerializer
    permission_classes = [AllowAny]

    pagination_class = PageNumberPagination
    pagination_class.page_size = 9
    pagination_class.page_query_param = 'pagenum'
    pagination_class.page_size_query_param ='size'
    pagination_class.max_page_size = 10

    def get_permissions(self):
        self.permission_classes = [AllowAny]

        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]

        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


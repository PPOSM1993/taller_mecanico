from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .models import Category
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.order_by('pk')
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        self.permission_classes = [AllowAny]

        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]

        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()




    @action(detail=False, methods=['GET'], permission_classes = [AllowAny])
    def list_categories(self, request):
        list_categories = Category.objects.all()

        serializer = self.get_serializer(list_categories, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST', 'DELETE'], url_path='create_category', permission_classes = [IsAuthenticated])
    def create_category(self, request, *args, **kwargs):
        return Response(serializer.data)

        
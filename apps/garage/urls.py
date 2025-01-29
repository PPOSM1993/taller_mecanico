from django.urls import path
from rest_framework.routers import DefaultRouter
from .import views

urlpatterns = [
]

router = DefaultRouter()
router.register('categories', views.CategoryViewSet),
router.register('brands', views.BrandViewSet),
router.register('car', views.CarViewSet),
urlpatterns += router.urls
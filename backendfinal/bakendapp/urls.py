from django.urls import path, include
from rest_framework import routers
from .views import ProductoViewSet, TestimonioViewSet, MensajeContactoViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'testimonios', TestimonioViewSet)
router.register(r'contacto', MensajeContactoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/productos/', views.ProductoListView.as_view(), name='producto-list'),
]
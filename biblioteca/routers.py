from rest_framework.routers import DefaultRouter

from .views import LibroViewSet, ResenaViewSet

router = DefaultRouter()
router.register(r"libros", LibroViewSet, basename="libro")
router.register(r"resenas", ResenaViewSet, basename="resena")

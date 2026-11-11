from rest_framework import permissions, viewsets

from .models import Libro, Resena
from .serializers import LibroSerializer, ResenaSerializer


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ResenaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer
    permission_classes = [permissions.IsAuthenticated]

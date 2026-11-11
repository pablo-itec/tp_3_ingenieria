from rest_framework import serializers

from .models import Libro, Resena


class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = [
            "id",
            "libro",
            "texto",
            "calificacion",
            "creado_en",
        ]
        read_only_fields = ["id", "creado_en"]


class LibroSerializer(serializers.ModelSerializer):
    resenas = ResenaSerializer(many=True, read_only=True)

    class Meta:
        model = Libro
        fields = [
            "id",
            "titulo",
            "autor",
            "isbn",
            "anio_publicacion",
            "disponible",
            "creado_en",
            "resenas",
        ]
        read_only_fields = ["id", "creado_en"]

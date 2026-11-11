# TP3 - API REST de Biblioteca (Django + DRF)

Tercer práctico: implementación de ViewSets, enrutamiento con `routers.py`, autenticación JWT (`djangorestframework-simplejwt`) y control de permisos con `permission_classes`.

## Modelos

- `Libro`: título, autor, ISBN, año de publicación, disponibilidad y fecha de creación.
- `Resena`: relación ForeignKey con `Libro`, texto de la reseña, calificación numérica y fecha de creación.

## Requisitos

- [uv](https://docs.astral.sh/uv/) instalado.

## Instalación y uso

```bash
# Sincroniza el entorno e instala dependencias
uv sync

# Aplica las migraciones
uv run python manage.py migrate

# Crea un superusuario para autenticarte
uv run python manage.py createsuperuser

# Inicia el servidor
uv run python manage.py runserver
```

El servidor queda disponible en `http://localhost:8000/`.

## Autenticación (JWT)

| Método | Endpoint             | Descripción                              |
|--------|----------------------|------------------------------------------|
| POST   | `/api/token/`        | Obtener tokens (access y refresh)        |
| POST   | `/api/token/refresh/`| Refrescar el access token                |

Para acceder a endpoints protegidos, incluir en la cabecera del request:
`Authorization: Bearer <access_token>`

## Endpoints

| Método | Endpoint              | ViewSet (Tipo)           | Permisos                   | Acción                        |
|--------|-----------------------|--------------------------|----------------------------|-------------------------------|
| GET    | `/api/libros/`        | `LibroViewSet` (Model)   | Lectura libre              | Listar todos los libros       |
| POST   | `/api/libros/`        | `LibroViewSet` (Model)   | Requiere autenticación     | Crear un libro                |
| GET    | `/api/libros/<id>/`   | `LibroViewSet` (Model)   | Lectura libre              | Detalle de un libro           |
| PUT    | `/api/libros/<id>/`   | `LibroViewSet` (Model)   | Requiere autenticación     | Modificar un libro            |
| PATCH  | `/api/libros/<id>/`   | `LibroViewSet` (Model)   | Requiere autenticación     | Modificación parcial de libro |
| DELETE | `/api/libros/<id>/`   | `LibroViewSet` (Model)   | Requiere autenticación     | Eliminar un libro             |
| GET    | `/api/resenas/`       | `ResenaViewSet` (ReadOnly)| Requiere autenticación    | Listar reseñas                |
| GET    | `/api/resenas/<id>/`  | `ResenaViewSet` (ReadOnly)| Requiere autenticación    | Detalle de una reseña         |

## Estructura del proyecto

```
config/            # Configuración general (settings, urls)
biblioteca/        # App principal
├── models.py      # Modelos Libro y Resena
├── serializers.py # Serializers y anidación
├── views.py       # LibroViewSet y ResenaViewSet
├── routers.py     # Registro de ViewSets en DefaultRouter
└── urls.py        # Rutas del router y endpoints JWT
manage.py
pyproject.toml     # Dependencias del proyecto (uv)
```

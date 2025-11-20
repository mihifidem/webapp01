from django.urls import path
from .views import listar_personas

urlpatterns = [
    path('', listar_personas),
]

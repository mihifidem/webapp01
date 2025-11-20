from django.urls import path, include

urlpatterns = [
    path('personas/', include('personas.urls')),
]

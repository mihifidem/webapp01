from django.http import JsonResponse
from .models import Person

def listar_personas(request):
    data = list(Person.objects.values())
    return JsonResponse(data, safe=False)

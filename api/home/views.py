from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(('GET',))
def home(request):
    return JsonResponse({'health': 'OK'})

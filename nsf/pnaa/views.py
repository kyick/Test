from django.shortcuts import render
from .models import Route, Cell

# Create your views here.
def map(request):
    routes = Route.objects.all()
    cells = Cell.objects.all()
    return render(request, 'pnaa/google_map.html', {'routes': routes, 'cells': cells})

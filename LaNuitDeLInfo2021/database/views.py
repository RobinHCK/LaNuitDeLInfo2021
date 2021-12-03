from django.shortcuts import render
from .models import Ship, Person, Rescue, Image


def drop(request):
    return render(request, 'database/drop.html')


def search_ship(request):
    query = request.GET.get('query')
    if not query:
        ships = Ship.objects.all()
    else:
        ships= Ship.objects.filter(name_icontains=query)
    title = 'Résutats pour la requête %s'%query

    context = {
        'ships': ships,
        'title': title
    }
    return render(request, 'database/search.html', context)

from django.shortcuts import render
from .models import Ship, Person, Rescue, Image, extract_frist_image
views.py¶
from django.http import HttpResponseRedirect
from .forms import UploadFileForm


def drop(request):
    return render(request, 'database/drop.html')


def search_ship(request):
    query = request.GET.get('query')
    if not query:
        ships = Ship.objects.all()
    else:
        ships = Ship.objects.filter(name_icontains=query)
    title = 'Résutats pour la requête %s'%query

    ships = [extract_frist_image(ship) for ship in ships]
    context = {
        'ships': ships,
        'title': title
    }
    return render(request, 'database/search_ship.html', context)


def ship_detail(request, ship_id):
    ship = Ship.objects.get(pk=ship_id)
    images = [img.img for img in ship.images.all()]
    saving = ship.savor.all()
    rescues = ship.rescued_in.all()
    context = {
        'ship': ship,
        'image': images[0],
        'images': images[1:],
        'rescues': rescues,
        'saving': saving,
    }


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
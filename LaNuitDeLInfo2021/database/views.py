from django.shortcuts import render
from .models import Ship, Person, Rescue, Image, extract_frist_image
from .forms import ImageForm


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


def image_upload_view(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img = form.instance
            text = 'Traduction:'
        return render(request, 'database/drop.html', context={'form': form, 'img': img.img.path, 'text': text})
    form = ImageForm()
    return render(request, 'database/drop.html', context={'form': form})

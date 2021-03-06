from django.shortcuts import render
from .models import Ship, Person, Rescue, Image, extract_first_image
from .forms import ImageForm
from .ocr_main import main as ocr_main


def search_ship(request):
    query = request.GET.get('query')
    if not query:
        ships = Ship.objects.all()
    else:
        ships = Ship.objects.filter(name_icontains=query)
    title = 'Résutats pour la requête %s'%query

    ships = [extract_first_image(ship) for ship in ships]
    context = {
        'ships': ships,
        'title': title
    }
    return render(request, 'database/search_ship.html', context)


def detail_ship(request, ship_id):
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
    return render(request, 'database/detail_ship.html', context)


def search_person(request):
    query = request.GET.get('query')
    if not query:
        persons = Person.objects.all()
    else:
        persons = Person.objects.filter(name_icontains=query)
    title = 'Résutats pour la requête %s'%query

    persons = [extract_first_image(person) for person in persons]
    context = {
        'persons': persons,
        'title': title
    }
    return render(request, 'database/search_person.html', context)


def detail_person(request, person_id):
    person = Person.objects.get(pk=person_id)
    images = [img.img for img in person.images.all()]
    saving = person.saved.all()
    rescues = person.distress.all()
    context = {
        'person': person,
        'image': images[0],
        'images': images[1:],
        'rescues': rescues,
        'saving': saving,
    }
    return render(request, 'database/detail_person.html', context)


def image_upload_view(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img = form.instance
            try:
                text = ocr_main(img.img.path)
            except:
                text = None
            if text is None or text == '':
                text = "Aucun élément n'a pu être extrait"

        return render(request, 'database/drop.html', context={'form': form, 'img': img, 'text': text})
    form = ImageForm()
    return render(request, 'database/drop.html', context={'form': form})


def submit_image(request):
    return render(request, 'database/thx.html')

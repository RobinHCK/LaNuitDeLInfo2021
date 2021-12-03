import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','LaNuitDeLInfo2021.settings')

import django
django.setup()
from django.core.files import File
from urllib import request
from django.core.files.base import ContentFile
import datetime

from database.models import Person, Ship, Rescue, Image


def add_Person(name, images):
    p = Person(first_name=name[1], given_name=name[0])
    p.save()
    p.images.set(images)
    p.save()
    return p


def add_Ship(name, images):
    s = Ship.objects.create(name=name)
    s.save()
    s.images.set(images)
    s.save()
    return s


def add_Rescue(date, save_ship, rescued_ship, lifeguard, rescued, images):
    r = Rescue.objects.create(date=date, save_ship=save_ship, rescued_ship=rescued_ship,
                          lifeguard=lifeguard, rescued=rescued)
    r.save()
    r.images.set(images)
    r.save()
    return r


def add_Image(path):
    img = Image()

    with open(path, 'rb') as f:
        data = f.read()

    # obj.image is the ImageField
    img.img.save(os.path.basename(path), ContentFile(data))

    img.save()

    return img

def populate_db():
    dl_path = 'C:/Users/Lafabregue/Downloads/'
    persons_imgs = [dl_path+'Morel-Benjamin-Portrait.jpg',
                    dl_path+'Eugene-Charet-Portrait-781x1024.jpg',
                    dl_path+'J-JAnnekeyn-e1633881630206.png'
                    ]
    persons = [('Jacques-Benjamin', 'MOREL'),
               ('Eugène Jules Charles', 'CHARET'),
               ('Jacques François', 'Jannekeyn')
               ]

    persons_imgs_obj = [add_Image(url) for url in persons_imgs]

    persons_obj = [add_Person(p, [img]) for p, img in zip(persons, persons_imgs_obj)]

    ships = ['CHARLES-AMELIE', 'ALODIA']
    ships_imgs = [None, None]

    ships_obj = [add_Ship(s, [img]) for s, img in zip(ships, ships_imgs)]

    rescues = [(datetime.datetime(1878, 1, 8), None, ships_obj[0], persons_obj[2], None, None),
               (datetime.datetime(1885, 8, 29), None, ships_obj[1], persons_obj[2], None, None)]


if __name__ == "__main__":
    populate_db()


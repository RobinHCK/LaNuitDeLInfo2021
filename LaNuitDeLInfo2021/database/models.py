from django.db import models


# Create or retrieve a placeholder
def get_sentinel_ship():
    return Ship.objects.get_or_create(name="The flyhing Dutchman")[0]


# Create an additional method to return only the id - default expects an id and not a Model object
def get_sentinel_ship_pk():
    return get_sentinel_ship().pk


class Ship(models.Model):
    name = models.CharField(max_length=200, unique=True)

    # @classmethod
    # def get_default(cls):
    #     ghost_ship = cls.objects.get_or_create(name="The flyhing Dutchman")[0]
    #     return ghost_ship
    #
    # @classmethod
    # def get_default_pk(cls):
    #     return cls.get_default().pk

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Rescue(models.Model):
    date = models.DateTimeField()
    save_ship = models.ForeignKey(Ship, on_delete=models.SET_NULL, related_name='savor', default=None, null=True)
    rescued_ship = models.ForeignKey(Ship, on_delete=models.SET_NULL, related_name='rescued_in',
                                     default=None, null=True)
    # ship = models.ForeignKey(Ship, default=get_sentinel_ship(), on_delete=models.SET(get_sentinel_ship_pk()))
    # rescue_ship = models.ForeignKey(Ship, default=get_sentinel_ship(), on_delete=models.SET(get_sentinel_ship_pk()))
    lifeguard = models.ManyToManyField(Person, related_name='rescues', blank=True)
    rescued = models.ManyToManyField(Person, related_name='distresses', blank=True)

    def __str__(self):
        return 'Rescue of the ship {self.ship.name} the {self.date})'.format(self=self)

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.forms import ModelForm , ModelChoiceField


listNeighbours = [('non','1'), ('nap','2'),('nep','3')]


@python_2_unicode_compatible  # only if you need to support Python 2
class AirbnbRequest(models.Model):
    name = models.CharField(max_length=200)

    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    accomodates = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    bedrooms = models.IntegerField(default=0)
    beds = models.IntegerField(default=0)
    guestsIncluded = models.IntegerField(default=0)
    entireApartament = models.BooleanField(default=False)


    #selectors
    neighborhood = models.IntegerField(default=0)
    cancellationPolicy = models.IntegerField(default=0)
    apartamentType = models.IntegerField(default=0)
    typeOfRoom = models.IntegerField(default = 0)
    typeOfBed = models.IntegerField(default=0)

    #not in the form items
    pub_date = models.DateTimeField('date published')
    finalRecomendedPrice = models.DecimalField(default=0, decimal_places=2, max_digits=8)

    def __str__(self):
        return self.name            


@python_2_unicode_compatible  # only if you need to support Python 2
class Amenities(models.Model):
    AirbnbRequest = models.ForeignKey(AirbnbRequest, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name



from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Vehicle(models.Model):
    brand = models.CharField(max_length=40, blank=True, null=True)
    model = models.CharField(max_length=40, blank=True, null=True)
    year = models.IntegerField(null=True)
    color = models.CharField(max_length=40, blank=True, null=True)
    license_plate = models.CharField(max_length=40, blank=True, null=True)
    seats = models.IntegerField(null=True)
    owner = models.ForeignKey("accounts.User")

    def __str__(self):
        return "{0} - {1}".format(self.model, self.owner.get_full_name())


class Address(models.Model):
    latitude = models.CharField(max_length=20, blank=True)
    longitude = models.CharField(max_length=20, blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return "{0} - {1}".format(self.latitude, self.longitude)


PEER_SEAT = "PS"
FULL_CAR = "FC"
CONDITION = (
    (PEER_SEAT, _("Por puesto")),
    (FULL_CAR, _("Auto completo")),

)


class Offer(models.Model):
    departure_address = models.ForeignKey("rides.Address",
                                          related_name="departure")
    arrival_address = models.ForeignKey("rides.Address",
                                        related_name="arrival")
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField(blank=True, null=True)
    vehicle = models.ForeignKey("rides.Vehicle")
    condition = models.CharField(max_length=2, choices=CONDITION,
                                 default=PEER_SEAT)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    seats = models.IntegerField(null=True)
    owner = models.ForeignKey("accounts.User")

    def __str__(self):
        return "{0} - {1}".format(self.departure_address.text,
                                  self.owner.get_full_name())
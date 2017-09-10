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

DISPONIBLE = "Di"
RESERVADO = "Re"
CANCELADO = "Ca"
REALIZADO = "Re"
STATUS_RIDE = (
    (DISPONIBLE, _("Disponible")),
    (RESERVADO, _("Reservado")),
    (CANCELADO, _("Cancelado")),
    (REALIZADO, _("Realizado")),
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
    status = models.CharField(max_length=2, choices=STATUS_RIDE,
                              default=DISPONIBLE)
    owner = models.ForeignKey("accounts.User")
    date = models.DateTimeField(auto_now_add=True)
    demand = models.ForeignKey("rides.Demand", null=True, default=None, related_name="offers")
    def __str__(self):
        return "{0} - {1}".format(self.departure_address.text,
                                  self.owner.get_full_name())


class Demand(models.Model):
    departure_address = models.ForeignKey("rides.Address",
                                          related_name="departure_address")
    arrival_address = models.ForeignKey("rides.Address",
                                        related_name="departure_arrival")
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField(blank=True, null=True)
    condition = models.CharField(max_length=2, choices=CONDITION,
                                 default=PEER_SEAT)

    seats = models.IntegerField(null=True)
    status = models.CharField(max_length=2, choices=STATUS_RIDE,
                              default=DISPONIBLE)
    owner = models.ForeignKey("accounts.User")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1}".format(self.departure_address.text,
                                  self.owner.get_full_name())

class RequestPost(models.Model):
    text = models.TextField()
    owner = models.ForeignKey("accounts.User")
    offer = models.ForeignKey("rides.Offer", related_name="request_offer")
    date = models.DateTimeField(auto_now_add=True)
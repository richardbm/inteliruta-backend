from django.db import models

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
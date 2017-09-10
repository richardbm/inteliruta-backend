from django.contrib import admin
from rides import models
# Register your models here.

admin.site.register(models.Vehicle)
admin.site.register(models.Address)
admin.site.register(models.Offer)
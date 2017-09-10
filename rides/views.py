from django.shortcuts import render
from utils4geek.base.viewsets import ModelCrudViewSet
from rides import models as rides_models
from rides import serializers as rides_serializers
from rest_framework import permissions, viewsets
from utils4geek.base.permissions import IsUserActive


class MyVehiclesViewSet(viewsets.ModelViewSet):
    """
    List to view my vechiles
    """
    queryset = rides_models.Vehicle.objects.all()
    serializer_class = rides_serializers.VehicleSerializer
    permission_classes = (permissions.IsAuthenticated, IsUserActive,)

    def get_queryset(self):
        queryset = super(MyVehiclesViewSet, self).get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset



class MyOffersViewSet(viewsets.ModelViewSet):
    """
    List to view my offers
    """
    queryset = rides_models.Offer.objects.all()
    serializer_class = rides_serializers.RidesSerializer
    permission_classes = (permissions.IsAuthenticated, IsUserActive,)

    def get_queryset(self):
        queryset = super(MyOffersViewSet, self).get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset




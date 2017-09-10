from django_filters.rest_framework import DjangoFilterBackend
from rides import models as rides_models
from rides import serializers as rides_serializers
from rest_framework import permissions, viewsets, filters
from utils4geek.base.permissions import IsUserActive


class MyVehiclesViewSet(viewsets.ModelViewSet):
    """
    List to view my vechiles
    """
    queryset = rides_models.Vehicle.objects.all()
    serializer_class = rides_serializers.VehicleSerializer
    permission_classes = (permissions.IsAuthenticated, IsUserActive,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter)
    ordering = ("model",)
    search_fields = ('model', 'brand',)

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
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter)
    ordering = ("departure_date",)
    search_fields = ('arrival_address__text', 'departure_address__text',)
    filter_fields = ("status",)

    def get_queryset(self):
        queryset = super(MyOffersViewSet, self).get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class OffersViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List to view offers
    """
    queryset = rides_models.Offer.objects.all()
    serializer_class = rides_serializers.RidesSerializer
    permission_classes = (permissions.IsAuthenticated, IsUserActive,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter)
    ordering = ("departure_date",)
    search_fields = ('arrival_address__text', 'departure_address__text',)

    def get_queryset(self):
        queryset = super(OffersViewSet, self).get_queryset()
        queryset = queryset.filter(status=rides_models.DISPONIBLE)
        return queryset



class DemandsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List to view demands
    """
    queryset = rides_models.Demand.objects.all()
    serializer_class = rides_serializers.DemandSerializer
    permission_classes = (permissions.IsAuthenticated, IsUserActive,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter)
    ordering = ("departure_date",)
    search_fields = ('arrival_address__text', 'departure_address__text',)

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(status=rides_models.DISPONIBLE)
        return queryset


class MyDemandsViewSet(viewsets.ModelViewSet):
    """
    List to view my Demands
    """
    queryset = rides_models.Demand.objects.all()
    serializer_class = rides_serializers.DemandSerializer
    permission_classes = (permissions.IsAuthenticated, IsUserActive,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter)
    ordering = ("departure_date",)
    search_fields = ('arrival_address__text', 'departure_address__text',)
    filter_fields = ("status",)

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(owner=self.request.user)
        return queryset

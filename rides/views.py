from django_filters.rest_framework import DjangoFilterBackend
from rides import models as rides_models
from rides import serializers as rides_serializers
from rest_framework import permissions, viewsets, filters
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from utils4geek.base.permissions import IsUserActive


class MyVehiclesViewSet(viewsets.ModelViewSet):
    """
    List to view my vechiles
    """
    queryset = rides_models.Vehicle.objects.all()
    serializer_class = rides_serializers.VehicleSerializer
    permission_classes = (permissions.IsAuthenticated, IsUserActive,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,
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
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter)
    ordering = ("departure_date",)
    search_fields = ('arrival_address__text', 'departure_address__text',)
    filter_fields = ("status",)

    def get_queryset(self):
        queryset = super(MyOffersViewSet, self).get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset

    @detail_route(methods=["post"], permission_classes=permission_classes,
                  url_path="accept-request")
    def accept_request(self, request, *args, **kwargs):
        instance = self.get_object()
        request_id = request.data.get("request_id")
        request_post = rides_models.RequestPost.objects.get(id=request_id)
        instance.passenger.add(request_post.owner)
        if instance.offer_type == rides_models.FULL_CAR:
            instance.status = rides_models.RESERVADO
        elif instance.passenger.count == instance.seats:
            instance.status = rides_models.RESERVADO
            instance.save()
        data = {
            "detail": "accepted"
        }
        return Response(data, status=201)


class OffersViewSet(viewsets.ModelViewSet):
    """
    List to view offers
    """
    queryset = rides_models.Offer.objects.all()
    serializer_class = rides_serializers.RidesSerializer
    permission_classes = (permissions.IsAuthenticated, IsUserActive,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter)
    ordering = ("departure_date",)
    search_fields = ('arrival_address__text', 'departure_address__text',)
    http_method_names = ["get", "post"]

    def get_queryset(self):
        queryset = super(OffersViewSet, self).get_queryset()
        queryset = queryset.filter(status=rides_models.DISPONIBLE,
                                   offer_type=rides_models.PUBLICA)
        return queryset

    @detail_route(methods=["post"], permission_classes=permission_classes)
    def request(self, request, *args, **kwargs):
        instance = self.get_object()
        context = {
            "request": request
        }
        data = request.data.copy()
        data['offer'] = instance.id
        request_post = rides_serializers.RequestSerializer(data=data,
                                                           context=context)

        request_post.is_valid(raise_exception=True)
        request_post.save()
        return Response(request_post.data, status=201)


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

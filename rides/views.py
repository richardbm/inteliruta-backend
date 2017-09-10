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
        queryset = queryset.filter(status=rides_models.DISPONIBLE)
        return queryset

    @detail_route(methods=["post"], permission_classes=permission_classes)
    def request(self, request, *args, **kwargs):
        instance = self.get_object()
        context = {
            "request": request
        }
        data = request.data.copy()
        data['offer_id'] = instance
        request_post = rides_serializers.RequestSerializer(data=data,
                                                           context=context)

        request_post.is_valid(raise_exception=True)
        request_post.save()
        return Response(request_post.data, status=201)






from rest_framework import serializers
from rides import models as rides_models


class VehicleSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = rides_models.Vehicle
        fields = ('id', 'brand', 'model', 'year', 'color',
                  'license_plate', 'seats', 'owner')


class RidesSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = rides_models.Vehicle
        fields = '__all__'



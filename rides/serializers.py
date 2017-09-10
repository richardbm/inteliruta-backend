from rest_framework import serializers
from rides import models as rides_models


class RidesSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = rides_models.Vehicle
        fields = ('brand', 'model', 'year', 'color',
                  'license_plate', 'seats', 'owner')



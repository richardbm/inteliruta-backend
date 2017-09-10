from rest_framework import serializers
from rides import models as rides_models
from utils4geek.base.serializers import DateTimeFieldWihTZ


class VehicleSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = rides_models.Vehicle
        fields = ('id', 'brand', 'model', 'year', 'color',
                  'license_plate', 'seats', 'owner')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = rides_models.Address
        fields = ('latitude', 'longitude', 'text',)


class RidesSerializer(serializers.ModelSerializer):
    departure_date = DateTimeFieldWihTZ(format='%Y-%m-%dT%H:%M:%S%z')
    arrival_date = DateTimeFieldWihTZ(format='%Y-%m-%dT%H:%M:%S%z', allow_null=True)
    departure_address = AddressSerializer()
    arrival_address = AddressSerializer()
    condition_display = serializers.SerializerMethodField()
    vehicle = VehicleSerializer(read_only=True)
    vehicle_id = serializers.IntegerField(required=True, write_only=True)
    status_display = serializers.SerializerMethodField()
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def get_condition_display(self, obj):
        return obj.get_condition_display()

    def get_status_display(self, obj):
        return obj.get_status_display()

    def validate_vehicle_id(self, vehicle_id):
        Vehicle = rides_models.Vehicle
        owner = self.context['request'].user
        queryset = Vehicle.objects.filter(id=vehicle_id, owner=owner)
        if queryset.exists() is False:
            raise serializers.ValidationError("vehicle does not exists")
        return vehicle_id

    class Meta:
        model = rides_models.Offer
        fields = '__all__'

    def create(self, validated_data):
        departure_address_data = validated_data.pop("departure_address")
        arrival_address_data = validated_data.pop("arrival_address")
        departure_address = AddressSerializer(data=departure_address_data)
        arrival_address = AddressSerializer(data=arrival_address_data)
        departure_address.is_valid()
        arrival_address.is_valid()
        departure_address.save()
        arrival_address.save()
        validated_data["departure_address"] = departure_address.instance
        validated_data["arrival_address"] = arrival_address.instance
        instance = super(RidesSerializer, self).create(validated_data)
        return instance

    def update(self, instance, validated_data):
        departure_address_data = validated_data.pop("departure_address")
        arrival_address_data = validated_data.pop("arrival_address")
        departure_address = AddressSerializer(instance.departure_address,
                                              data=departure_address_data)
        arrival_address = AddressSerializer(instance.arrival_address,
                                            data=arrival_address_data)
        departure_address.is_valid()
        arrival_address.is_valid()
        departure_address.save()
        arrival_address.save()
        instance = super(RidesSerializer, self).update(instance, validated_data)
        return instance


class RequestSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = rides_models.RequestPost
        fields = ("id", "text", "owner", "date", "offer_id",)

from rest_framework import serializers
from rides import models as rides_models
from utils4geek.base.serializers import DateTimeFieldWihTZ
from accounts.serializers import ProfleSerializer

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


class RequestSerializer(serializers.ModelSerializer):
    date = DateTimeFieldWihTZ(format='%Y-%m-%dT%H:%M:%S%z', read_only=True)
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = rides_models.RequestPost
        fields = ("id", "text", "owner", "date", "offer",)


class RidesSerializer(serializers.ModelSerializer):
    departure_date = DateTimeFieldWihTZ(format='%Y-%m-%dT%H:%M:%S%z')
    departure_address = AddressSerializer()
    arrival_address = AddressSerializer()
    condition_display = serializers.SerializerMethodField()
    vehicle = VehicleSerializer(read_only=True)
    vehicle_id = serializers.IntegerField(required=True, write_only=True)
    demand_id = serializers.IntegerField(required=False, write_only=True)
    accepted_offer_id = serializers.IntegerField(required=False, write_only=True)
    status_display = serializers.SerializerMethodField()
    type_display = serializers.SerializerMethodField()
    request_offer = serializers.SerializerMethodField()
    passenger = ProfleSerializer(many=True, read_only=True)
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def get_request_offer(self, obj):
        request_offer = obj.request_offer.all()
        data = RequestSerializer(request_offer, many=True).data
        return data

    def get_condition_display(self, obj):
        return obj.get_condition_display()

    def get_type_display(self, obj):
        return obj.get_offer_type_display()

    def get_status_display(self, obj):
        return obj.get_status_display()

    def validate_vehicle_id(self, vehicle_id):
        Vehicle = rides_models.Vehicle
        owner = self.context['request'].user
        queryset = Vehicle.objects.filter(id=vehicle_id, owner=owner)
        if queryset.exists() is False:
            raise serializers.ValidationError("vehicle does not exists")
        return vehicle_id

    def validate_demand_id(self, demand_id):
        try:
            rides_models.Demand.objects.get(id=demand_id)
        except rides_models.Demand.DoesNotExist:
            raise serializers.ValidationError("demand does not exists")
        return demand_id

    class Meta:
        model = rides_models.Offer
        exclude = ('arrival_date',)

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

        if validated_data.get("demand_id"):
            demand_id = validated_data.pop("demand_id")
            demand = rides_models.Demand.objects.get(id=demand_id)
            instance.demand = demand

        if validated_data.get("accepted_offer_id"):
            accepted_offer_id = validated_data.pop("accepted_offer_id")
            offer = rides_models.Offer.objects.get(id=accepted_offer_id)
            offer.status = rides_models.RESERVADO
            offer.passenger.add(instance.owner)
            offer.save()


        
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


class DemandSerializer(serializers.ModelSerializer):
    departure_date = DateTimeFieldWihTZ(format='%Y-%m-%dT%H:%M:%S%z')
    departure_address = AddressSerializer()
    arrival_address = AddressSerializer()
    condition_display = serializers.SerializerMethodField()
    status_display = serializers.SerializerMethodField()
    offers = RidesSerializer(many=True, read_only=True)
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def get_condition_display(self, obj):
        return obj.get_condition_display()

    def get_status_display(self, obj):
        return obj.get_status_display()

    class Meta:
        model = rides_models.Demand
        exclude = ('arrival_date',)

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
        instance = super(DemandSerializer, self).create(validated_data)
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
        instance = super(DemandSerializer, self).update(instance, validated_data)
        return instance
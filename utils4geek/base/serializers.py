from rest_framework import serializers
from django.utils import timezone


class DateTimeFieldWihTZ(serializers.DateTimeField):
    """
    date = DateTimeFieldWihTZ(format='%Y-%m-%dT%H:%M:%S%z')
    e.g: "2017-09-09T15:30:00-04:00"
    """
    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(DateTimeFieldWihTZ, self).to_representation(value)
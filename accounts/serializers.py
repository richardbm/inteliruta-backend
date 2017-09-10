from rest_framework import serializers
from accounts.models import User


class ProfleSerializer(serializers.ModelSerializer):
    hometown = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'facebook_picture_url', 'username', 'first_name',
                  'last_name', 'email', 'is_staff', 'hometown',)

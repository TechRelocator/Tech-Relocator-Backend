from rest_framework import serializers
from .models import User_Profile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Profile
        fields = "__all__"
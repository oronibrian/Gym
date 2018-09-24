
from django.contrib.auth.models import User
from rest_framework import serializers
# from .models import Job, Bid, GeoLocation, Notification, Wallet, Transactions
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from rest_framework.views import exception_handler
from django.core.exceptions import ValidationError


#Aauthentication serializer

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = [
            'pk',
            'url',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_staff', 
        ]

    def validate(self, attrs):
        password = attrs['password']
        if len(password) < 9:
            raise serializers.ValidationError("password is too short.")
        return attrs

    def create(self, validated_data):
        ModelClass = self.Meta.model
        instance = ModelClass.objects.create_user(**validated_data)
        return instance
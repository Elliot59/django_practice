from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields ='__all__'
        depth = 1

class UserSignup(serializers.ModelSerializer):
    def create(self, validated_data):
        user = Player(
        name = validated_data['name'],
        age = validated_data['age'],
        height = validated_data['height'],
        email = validated_data['email'],
        password = validated_data['password'],
        pwd2 = validated_data['pwd2'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
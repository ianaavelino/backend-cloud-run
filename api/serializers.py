from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ["id", "nome", "email", "senha"]

    def create(self, validated_data):
        validated_data["senha"] = make_password(
            validated_data["senha"]
        )
        return Usuario.objects.create(**validated_data)
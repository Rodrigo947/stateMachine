from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import serializers

user_model = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, required=True)
    cpf = serializers.CharField(max_length=11, required=True)
    pis = serializers.CharField(max_length=11, required=True)
    password = serializers.CharField(max_length=128, required=True)

    first_name = serializers.CharField(max_length=30, required=True)
    last_name = serializers.CharField(max_length=30, required=True)

    pais = serializers.CharField(max_length=255, required=False)
    estado = serializers.CharField(max_length=255, required=False)
    municipio = serializers.CharField(max_length=255, required=False)
    cep = serializers.CharField(max_length=8, required=False)
    rua = serializers.CharField(max_length=255, required=False)
    numero = serializers.CharField(max_length=255, required=False)
    complemento = serializers.CharField(max_length=255, required=False)

    class Meta:
        model = user_model
        fields = [
            "email",
            "cpf",
            "pis",
            "password",
            "first_name",
            "last_name",
            "pais",
            "estado",
            "municipio",
            "cep",
            "rua",
            "numero",
            "complemento",
        ]

    def create(self, validated_data):
        try:
            user_model.objects.get(
                Q(email__iexact=validated_data["email"])
                | Q(cpf__iexact=validated_data["cpf"])
                | Q(pis__iexact=validated_data["pis"])
            )
            return False
        except user_model.DoesNotExist:
            user = user_model.objects.create(**validated_data)
            user.set_password(validated_data["password"])
            user.save()
            return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = [
            "email",
            "cpf",
            "pis",
            "password",
            "first_name",
            "last_name",
            "pais",
            "estado",
            "municipio",
            "cep",
            "rua",
            "numero",
            "complemento",
        ]

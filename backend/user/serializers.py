from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import serializers

user_model = get_user_model()


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, required=True)
    cpf = serializers.CharField(max_length=11, required=True)
    pis = serializers.CharField(max_length=11, required=True)
    password = serializers.CharField(max_length=128, required=True, style={"input_type": "password"})

    first_name = serializers.CharField(max_length=30, required=True)
    last_name = serializers.CharField(max_length=30, required=True)

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


class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = [
            "email",
            "cpf",
            "pis",
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


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = [
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


class UserChangePasswordBaseSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128, required=True, style={"input_type": "password"})
    new_password = serializers.CharField(max_length=128, required=True, style={"input_type": "password"})
    repeat_password = serializers.CharField(max_length=128, required=True, style={"input_type": "password"})


class UserChangePasswordSerializer(UserChangePasswordBaseSerializer):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

    def validate(self, attrs):
        if not self.user.check_password(attrs["old_password"]):
            raise serializers.ValidationError({"message": "Senha atual incorreta"})
        if attrs["old_password"] == attrs["new_password"]:
            raise serializers.ValidationError({"message": "Senha antiga n??o pode ser a mesma da nova"})
        if attrs["new_password"] != attrs["repeat_password"]:
            raise serializers.ValidationError({"message": "Senhas n??o correspodem"})
        if len(attrs["new_password"]) < 8:
            raise serializers.ValidationError({"message": "Senha n??o pode ser menor que 8 caracteres"})
        return attrs

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class TokenObtainPairResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class TokenRefreshResponseSerializer(serializers.Serializer):
    access = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()

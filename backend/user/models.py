import uuid

import django.contrib.auth.validators
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, cpf, pis, password, **extra_fields):
        """
        Create and save a user with the given email, cpf, pis, and password.
        """
        if not email:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)

        user = self.model(email=email, cpf=cpf, pis=pis, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, cpf, pis, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, cpf, pis, password, **extra_fields)

    def create_superuser(self, email, cpf, pis, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self._create_user(email, cpf, pis, password, **extra_fields)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Dados de login
    email = models.EmailField(unique=True, max_length=255, editable=False)
    cpf = models.CharField(unique=True, max_length=11, editable=False)
    pis = models.CharField(unique=True, max_length=11, editable=False)

    # Endereço
    pais = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    cep = models.CharField(max_length=8)
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255)

    # Controle de acesso
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name="updated date",
        blank=True,
        null=True,
    )

    username = (
        models.CharField(
            max_length=150,
            validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
            verbose_name="username",
        ),
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["cpf", "pis", "password"]

    objects = UserManager()

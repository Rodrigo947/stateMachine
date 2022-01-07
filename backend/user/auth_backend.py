from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

user_model = get_user_model()


class AuthBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):

        if email is None or password is None:
            return None

        try:
            user = user_model.objects.get(Q(email__iexact=email) | Q(cpf__iexact=email) | Q(pis__iexact=email))
        except user_model.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user

        return None

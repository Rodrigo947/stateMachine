from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from user.serializers import SignupSerializer, UserSerializer

user_model = get_user_model()


class Signup(APIView):
    """
    Cria um novo usuário
    """

    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            if serializer.create(serializer.validated_data):
                return Response({"message": "Usuário criado"}, status=status.HTTP_201_CREATED)

            return Response({"message": "Usuário existente"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class All(APIView):
    """
    Lista todos os Usuários
    """

    def get(self, request, format=None):
        users = User.objects.filter(is_superuser=False)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

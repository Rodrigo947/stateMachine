from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.serializers import (
    SignUpSerializer,
    TokenObtainPairResponseSerializer,
    TokenRefreshResponseSerializer,
    UserChangePasswordBaseSerializer,
    UserChangePasswordSerializer,
    UserEditSerializer,
    UserMeSerializer,
)

user_model = get_user_model()


class SignUp(APIView):
    """
    Cria um novo usuário

    Retorna uma mensagem de erro ou cria o usuário
    """

    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer

    @swagger_auto_schema(
        request_body=SignUpSerializer,
        responses={201: "Usuário criado", 400: "Usuário já existe"},
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data, user=request.user)

        if serializer.is_valid():
            if serializer.create(serializer.validated_data):
                return Response({"message": "Usuário criado"}, status=status.HTTP_201_CREATED)

            return Response({"message": "Usuário já existe"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserMe(APIView):
    """
    Recupera informações gerais do usuário.

    Necessário fornecer um token Bearer no Header
    Use a rota /api/auth/token/ para recuperar o token
    """

    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = UserMeSerializer

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: UserMeSerializer,
            status.HTTP_401_UNAUTHORIZED: "Token não informado ou inválido",
        },
    )
    def get(self, request):
        return Response(self.serializer_class(request.user).data)


class UserEdit(APIView):
    """
    Atualiza dados cadastrais

    Dados de endereço e nome podem ser alterados
    """

    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = UserEditSerializer

    @swagger_auto_schema(
        request_body=UserEditSerializer,
        responses={
            status.HTTP_200_OK: "Dados alterados",
            status.HTTP_401_UNAUTHORIZED: "Token não informado ou inválido",
        },
    )
    def post(self, request):
        serializer = self.serializer_class(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserChangePassword(APIView):
    """
    Mudar senhas

    A antiga senha deve ser passada com a nova senha e sua repetição
    """

    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = UserChangePasswordSerializer

    @swagger_auto_schema(
        request_body=UserChangePasswordBaseSerializer,
        responses={
            status.HTTP_200_OK: "Senha Alterada",
            status.HTTP_400_BAD_REQUEST: "Senha atual incorreta | Senha antiga não pode ser a mesma da nova | Senhas não correspodem",
            status.HTTP_401_UNAUTHORIZED: "Token não informado ou inválido",
        },
    )
    def post(self, request):
        user = request.user
        serializer = self.serializer_class(data=request.data, user=user)
        if serializer.is_valid():
            user.set_password(serializer.data["new_password"])
            user.save()
            return Response({"message": "Senha alterada"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDesactivate(APIView):
    """
    Desativa o usuário

    Desativa o usuário que fez a requisição
    Necessário fornecer um token Bearer no Header
    Use a rota /api/auth/token/ para recuperar o token
    """

    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "Usuário desativado",
            status.HTTP_401_UNAUTHORIZED: "Token não informado ou inválido",
        },
    )
    def post(self, request):
        user = request.user
        user.is_active = False
        user.save()

        return Response({"message": "Usuário desativado"}, status=status.HTTP_200_OK)


class DecoratedTokenObtainPairView(TokenObtainPairView):
    """
    Token e refresh token do usuário

    A partir do email,cpf ou pis (O campo email pode receber qualquer uma das 3 informações)
    e senha retorna o token e o refresh token do usuário
    """

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: TokenObtainPairResponseSerializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenRefreshView(TokenRefreshView):
    """
    Atualiza o token usuário

    A partir do refresh token do usuário
    retorna o novo token
    """

    @swagger_auto_schema(responses={status.HTTP_200_OK: TokenRefreshResponseSerializer})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

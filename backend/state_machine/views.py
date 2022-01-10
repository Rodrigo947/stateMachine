from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from state_machine.models import StateMachine
from state_machine.serializers import StateMachineCreateSerializer, StateMachineSerializer


class StateMachineView(APIView):
    """
    Retorna uma máquina de estado
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = StateMachineSerializer

    @swagger_auto_schema(
        request_body=StateMachineSerializer,
        responses={201: "Dados da máquina", 400: "Dados inválidos"},
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            machine = StateMachine.objects.get(pk=serializer.validated_data["id"])
            return Response({machine.id, machine.name}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StateMachineCreate(APIView):
    """
    Cria e retorna uma máquina de estado
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = StateMachineCreateSerializer

    @swagger_auto_schema(
        request_body=StateMachineCreateSerializer,
        responses={201: "Máquina de estado criada", 400: "Dados inválidos"},
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            machine = serializer.save(id_user=request.user)
            data_response = {"message": "Máquina de estado criada", "data": {"id": machine.id, "name": machine.name}}
            return Response(data_response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

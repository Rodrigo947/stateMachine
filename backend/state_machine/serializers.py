from rest_framework import serializers

from state_machine.models import StateMachine


class StateMachineSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)


class StateMachineCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateMachine
        fields = ["name"]

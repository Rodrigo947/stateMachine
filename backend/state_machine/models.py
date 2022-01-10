import uuid

from django.db import models
from user.models import User


class StateMachine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="id_user")

    class Meta:
        db_table = "state_machine"


class State(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    first_state = models.BooleanField()
    id_state_machine = models.ForeignKey(StateMachine, on_delete=models.CASCADE, db_column="id_state_machine")

    class Meta:
        db_table = "state"


class LastState(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_state_machine = models.ForeignKey(StateMachine, on_delete=models.CASCADE, db_column="id_state_machine")
    id_state = models.ForeignKey(State, on_delete=models.CASCADE, db_column="id_state")

    class Meta:
        db_table = "last_state"


class Transition(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    id_state_origin = models.ForeignKey(
        State, on_delete=models.CASCADE, related_name="id_state_origin", db_column="id_state_origin"
    )
    id_state_destiny = models.ForeignKey(
        State, on_delete=models.CASCADE, related_name="id_state_destiny", db_column="id_state_destiny"
    )

    class Meta:
        db_table = "transition"

# Generated by Django 3.2.11 on 2022-01-10 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('first_state', models.BooleanField()),
            ],
            options={
                'db_table': 'state',
            },
        ),
        migrations.CreateModel(
            name='Transition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('id_state_destiny', models.ForeignKey(db_column='id_state_destiny', on_delete=django.db.models.deletion.CASCADE, related_name='id_state_destiny', to='state_machine.state')),
                ('id_state_origin', models.ForeignKey(db_column='id_state_origin', on_delete=django.db.models.deletion.CASCADE, related_name='id_state_origin', to='state_machine.state')),
            ],
            options={
                'db_table': 'transition',
            },
        ),
        migrations.CreateModel(
            name='StateMachine',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('id_user', models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'state_machine',
            },
        ),
        migrations.AddField(
            model_name='state',
            name='id_state_machine',
            field=models.ForeignKey(db_column='id_state_machine', on_delete=django.db.models.deletion.CASCADE, to='state_machine.statemachine'),
        ),
        migrations.CreateModel(
            name='LastState',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('id_state', models.ForeignKey(db_column='id_state', on_delete=django.db.models.deletion.CASCADE, to='state_machine.state')),
                ('id_state_machine', models.ForeignKey(db_column='id_state_machine', on_delete=django.db.models.deletion.CASCADE, to='state_machine.statemachine')),
            ],
            options={
                'db_table': 'last_state',
            },
        ),
    ]
from django.urls import path

from state_machine import views

urlpatterns = [
    path("state-machine/", views.StateMachineView.as_view(), name="Get or Create State Machine"),
    path("state-machine/create/", views.StateMachineCreate.as_view(), name="Get or Create State Machine"),
]

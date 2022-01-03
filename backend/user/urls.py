from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from user import views

urlpatterns = [
    path("signup/", views.Signup.as_view(), name="signup"),
    path("all/", views.All.as_view(), name="all"),
]

"""
path("login/", views.Login.as_view(), name="login"),
path("logout/", views.Logout.as_view(), name="logout"),
path("user/me/", views.UserMe.as_view(), name="user-me"),
path("user/edit/", views.UserEdit.as_view(), name="user-edit"),
path("user/desactivate/", views.UserDesactivate.as_view(), name="user-desactivate"),
"""


urlpatterns = format_suffix_patterns(urlpatterns)

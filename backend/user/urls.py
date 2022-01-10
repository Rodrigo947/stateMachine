from django.urls import path

from user import views

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="Sign Up"),
    path("user/me/", views.UserMe.as_view(), name="User Me"),
    path("user/edit/", views.UserEdit.as_view(), name="User Edit"),
    path("user/change-password/", views.UserChangePassword.as_view(), name="User Change Password"),
    path("user/deactivate/", views.UserDeactivate.as_view(), name="User Deactivate"),
    path("auth/token/", views.DecoratedTokenObtainPairView.as_view(), name="Token"),
    path("auth/token/refresh/", views.DecoratedTokenRefreshView.as_view(), name="Token Refresh"),
]

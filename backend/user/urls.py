from django.urls import path

from user import views

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="Sign Up"),
    path("user/me/", views.UserMe.as_view(), name="User Me"),
    path("user/edit/", views.UserEdit.as_view(), name="User Edit"),
    path("user/change-passoword/", views.UserChangePassword.as_view(), name="User Change Password"),
    path("user/desactivate/", views.UserDesactivate.as_view(), name="User Desactivate"),
    path("token/", views.DecoratedTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", views.DecoratedTokenRefreshView.as_view(), name="token_refresh"),
]

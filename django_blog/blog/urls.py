from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile, CustomLoginView, CustomLogoutView

app_name = "blog"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
]

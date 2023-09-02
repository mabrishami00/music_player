from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path("/register", view.UserRegisterView.as_view(), name="register"),
    path("/login", view.UserLoginView.as_view(), name="login"),
]

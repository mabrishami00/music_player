from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.UserSignUpView.as_view(), name="signup"),
    path("signin/", views.UserSignInView.as_view(), name="signin"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("profile/", views.UserProfileView.as_view(), name="profile"),
    ]

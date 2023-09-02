from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("songs.urls", namespace="songs")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("interactions/", include("interactions.urls", namespace="interactions")),
]
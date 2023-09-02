from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("admin", namespace="songs")),
    path("accounts/", include("admin", namespace="accounts")),
    path("interactions/", include("admin", namespace="interactions")),
]
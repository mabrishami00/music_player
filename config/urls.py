from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("songs.urls", namespace="songs")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("interactions/", include("interactions.urls", namespace="interactions")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
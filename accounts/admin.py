from django.contrib import admin
from .forms import (
    CustomUserChangeForm,
    CustomUserCreationForm,
    ArtistCreationForm,
    ArtistChangeForm,
    UserLoginForm
)
from .models import BaseUser, User, Artist
from django.contrib.auth.admin import UserAdmin
import copy

class BaseUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "is_active",
    )
    list_filter = (
        "username",
        "email",
        "is_active",
    )
    fieldsets = [
        [None, {"fields": ["username", "name", "email", "password"]}],
        [
            "Permissions",
            {"fields": ["is_admin", "is_active", "groups", "user_permissions"]},
        ],
    ]
    add_fieldsets = [
        [
            None,
            {
                "classes": ("wide",),
                "fields": [
                    "username",
                    "name",
                    "email",
                    "password1",
                    "password2",
                    "is_admin",
                    "is_active",
                    "groups",
                    "user_permissions",
                ]
            },
        ],
    ]
    search_fields = ("email",)
    ordering = ("joined",)


class UserAdmin(BaseUserAdmin):
    fieldsets = copy.deepcopy(BaseUserAdmin.fieldsets)
    fieldsets[0][1]["fields"].insert(4, "status")
    fieldsets[0][1]["fields"].insert(5, "image")
    add_fieldsets = copy.deepcopy(BaseUserAdmin.add_fieldsets)
    add_fieldsets[0][1]["fields"].insert(4, "status")
    add_fieldsets[0][1]["fields"].insert(5, "image")


class ArtistAdmin(BaseUserAdmin):
    fieldsets = copy.deepcopy(BaseUserAdmin.fieldsets)
    fieldsets[0][1]["fields"].insert(4, "image")
    fieldsets[0][1]["fields"].insert(6, "band")
    add_fieldsets = copy.deepcopy(BaseUserAdmin.add_fieldsets)
    add_fieldsets[0][1]["fields"].insert(4, "image")
    add_fieldsets[0][1]["fields"].insert(6, "band")


admin.site.register(BaseUser, BaseUserAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Artist, ArtistAdmin)

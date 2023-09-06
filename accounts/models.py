from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from songs.models import Song
from .managers import MyUserManager


class BaseUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    bio = models.TextField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    joined = models.DateTimeField(auto_now_add=True)
    
    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("name",)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class User(BaseUser):
    MEMBERSHIP_CHOICES = (
        ('V', 'VIP'),
        ('F', 'FREE'),
    )
    image = models.ImageField(upload_to="User", null=True, blank=True)
    status = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default="F")

class Band(models.Model):
    name = models.CharField(max_length=50)


class Artist(BaseUser):
    image = models.ImageField(upload_to="Artist",null=True, blank=True)
    band = models.ForeignKey(Band, on_delete=models.SET_NULL, null=True, blank=True)

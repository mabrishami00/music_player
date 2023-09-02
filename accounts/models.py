from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from songs.models import Song
from .managers import MyUserManager
# Create your models here.

class BaseUser(AbstractBaseUser):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

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

    # class Meta:
    #     abstract = True

class User(BaseUser):
    image = models.ImageField(upload_to="User", null=True, blank=True)
    is_vip = models.BooleanField(default=False)

class Band(models.Model):
    name = models.CharField(max_length=50)


class Artist(BaseUser):
    image = models.ImageField(upload_to="Artist")
    song = models.ManyToManyField(Song)
    Band = models.ForeignKey(Band, on_delete=models.SET_NULL, null=True, blank=True)

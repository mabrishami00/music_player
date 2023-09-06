from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import BaseUser, User, Artist
from django import forms


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "sign__input", "placeholder": "Password"}
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "sign__input", "placeholder": "Confirm Password"}
        ),
    )
    is_agree = forms.BooleanField(
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                "id": "remember",
                "name": "remember",
            }
        ),
    )

    def clean_is_agree(self):
        is_agree = self.cleaned_data["is_agree"]
        if not is_agree:
            raise forms.ValidationError("You must check this box!")
        return is_agree

    class Meta:
        model = User
        fields = ("username", "email", "name")

        widgets = {
            "username": forms.TextInput(
                attrs={"class": "sign__input", "placeholder": "Username"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "sign__input", "placeholder": "Email"}
            ),
            "name": forms.TextInput(
                attrs={"class": "sign__input", "placeholder": "Name"}
            ),
        }


class UserLoginForm(forms.Form):
    is_artist = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "id": "is_artist",
                "name": "is_artist",
            }
        ),required=False
    )
    username_or_email = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "sign__input", "placeholder": "Username"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "sign__input", "placeholder": "Password"}
        ),
    )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email", "name")


class ArtistCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "name")


class ArtistChangeForm(UserChangeForm):
    class Meta:
        model = Artist
        fields = ("username", "email", "name")

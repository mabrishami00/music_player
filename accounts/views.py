from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreationForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from .models import User, Artist
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
class UserSignUpView(View):
    form_class = CustomUserCreationForm

    def dispatch(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            return redirect("songs:home")
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {"form": form}
        return render(request, "accounts/signup.html", context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = form.save(commit=False)
            user.set_password(cd["password1"])
            user.save()
            subject = 'Welcome'
            message = f'Welcome {user.name}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list)
            return redirect("songs:home")
        
        else:
            form = self.form_class(request.POST)
            context = {"form": form}
            return render(request, "accounts/signup.html", context=context)


class UserSignInView(View):
    form_class = UserLoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            return redirect("songs:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {"form": form}
        return render(request, "accounts/signin.html", context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username_or_email = cd.get('username_or_email')
            password = cd.get('password')
            is_artist = cd.get('is_artist')
            print(is_artist)
            user = authenticate(request, user_type=is_artist ,username=username_or_email, password=password)
            if user is not None:
                login(request, user)
                return redirect("songs:home")
            else :
                return redirect("accounts:signin")

        else:
            context = {"form": form}
            return render(request, "accounts/signin.html", context=context)


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("songs:home")


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "accounts/profile.html")
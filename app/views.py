from django.shortcuts import render
from templates import *
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from .forms import *
from django.contrib.auth.models import User
from django.views.generic import CreateView


def home(request):

    template = 'index.html'
    return render(request, template)


class RegisterUserView(CreateView):

    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')
    success_msg = 'Пользователь успешно создан'


class AppLoginView(LoginView):

    template_name = 'auth.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home')


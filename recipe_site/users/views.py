from multiprocessing import AuthenticationError
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy

from users.forms import LoginFormUser

class MyLoginView(LoginView):
    authentication_form = LoginFormUser
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация на сайте'}

    def get_success_url(self):
        return reverse_lazy('recipe_site_app:index')
    
class LoginUser(LoginView):
    form_class = AuthenticationError
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}
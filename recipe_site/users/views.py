from multiprocessing import AuthenticationError
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import Group

from users.forms import LoginFormUser, RegistrationForm

class MyLoginView(LoginView):
    authentication_form = LoginFormUser
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация на сайте'}

    def get_success_url(self):
        return reverse_lazy('recipe_site_app:index')

class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'users/registration.html'
    extra_context = {'title': 'Регистрация на сайте'}

    def get_success_url(self):
        return reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        group = Group.objects.get(name='Кулинары')
        user.groups.add(group)
        return super().form_valid(form)

class LoginUser(LoginView):
    form_class = AuthenticationError
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}


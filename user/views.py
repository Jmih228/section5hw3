from django.shortcuts import render, redirect
from django.contrib.auth import logout
from user.models import User
from django.views.generic import CreateView, UpdateView
from user.forms import UserRegisterForm, UserProfileForm
from django.urls import reverse_lazy, reverse
from string import ascii_letters as letters, digits
from random import sample
from user.email_funcs import _send_mail_email, _send_mail_password

def get_new_password(request):
    password = ''.join(sample(letters + digits, 10))
    request.user.set_password(password)
    request.user.save()
    _send_mail_password(password, request.user.email)
    return redirect(reverse('user:login'))


def verification(request):
    pk = request.POST['pk']
    user = User.objects.get(pk=pk)
    user.is_verificated = True
    user.is_activated = True
    return redirect(reverse('user:profile'))


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        self.object = form.save()
        _send_mail_email(self.object.email)
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('user:profile')

    def get_object(self, queryset=None):
        return self.request.user


def logout_view(request):
    logout(request)
    return redirect('user:login')

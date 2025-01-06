from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from transactions.contants import send_mail_to_user
import datetime
from .forms import UserRegistrationForm, UserUpdateForm, UserPasswordChangeForm
# Create your views here.


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        current_datetime = datetime.datetime.now()

        messages.success(self.request, f"""Your password has been changed""")

        send_mail_to_user("You password has been changed", 'accounts/password_change_mail.html', {
            'time': current_datetime.strftime("%A, %B %d, %Y")
        }, self.request.user.email)

        return super().form_valid(form)


class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration_form.html'
    success_url = reverse_lazy("register")
    form_class = UserRegistrationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user=user)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    success_url = reverse_lazy("homepage")

    def get_success_url(self):
        return reverse_lazy("homepage")


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("homepage")


class UserBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
        return render(request, self.template_name, {'form': form})
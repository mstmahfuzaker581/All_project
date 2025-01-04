from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from .forms import RegisterUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def homePage(request):
    return render(request, 'home.html')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                messages.success(request, "User successfully registered")
                return redirect("homePage")
            else:
                messages.warning(request, "User registration failed")
                return redirect("register_user")
    else:
        form = RegisterUserForm()
    return render(request, 'registerPage.html', {'form': form, 'type': 'Register'})


def login_user(request):
    next_url = request.GET.get('next', '/')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully")
                return redirect(next_url)
            else:
                messages.warning(request, "Wrong credentials")
                return redirect("login_user")
    else:
        form = AuthenticationForm()
    return render(request, 'registerPage.html', {'form': form, 'type': 'Login'})


def logout_user(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect("homePage")


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def change_password_with_old_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user=form.user)
            messages.success(request, "Password changed successfully")
            return redirect("homePage")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'registerPage.html', {'form': form, 'type': 'Change password'})


@login_required
def change_password_without_old_password(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user=form.user)
            messages.success(request, "Password changed successfully")
            return redirect("homePage")
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'RegisterPage.html', {'form': form, 'type': 'Change password'})
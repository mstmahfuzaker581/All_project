from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'required'}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'id': 'required'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UpdateUserForm(UserChangeForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'required'}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'id': 'required'}))
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
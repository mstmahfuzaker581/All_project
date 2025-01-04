from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Musician, Album


class MusiciansForm(ModelForm):
    class Meta:
        model = Musician
        fields = "__all__"


class AlbumsForm(ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
        help_texts = {
            "rating": "Rating can be 1 to 5",
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
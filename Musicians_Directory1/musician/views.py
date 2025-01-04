from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import MusiciansForm, AlbumsForm, RegisterForm
from .models import Album, Musician
# Create your views here.


@method_decorator(login_required, name="dispatch")
class AddMusiciansView(CreateView):
    model = Musician
    form_class = MusiciansForm
    template_name = 'addMusicians.html'
    success_url = reverse_lazy("view_musics")


@method_decorator(login_required, name="dispatch")
class AddAlbumView(CreateView):
    model = Album
    form_class = AlbumsForm
    template_name = "addAlbums.html"
    success_url = reverse_lazy("view_musics")


class DisplayMusicsView(ListView):
    model = Album
    template_name = 'viewMusics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = context['object_list']
        return context


@method_decorator(login_required, name="dispatch")
class DeleteAlbumView(DeleteView):
    model = Album
    success_url = reverse_lazy("view_musics")
    pk_url_kwarg = 'id'


@method_decorator(login_required, name="dispatch")
class UpdateAlbumView(UpdateView):
    model = Album
    form_class = AlbumsForm
    pk_url_kwarg = 'id'
    template_name = 'addAlbums.html'
    success_url = reverse_lazy("view_musics")


@method_decorator(login_required, name="dispatch")
class UpdateMusicsView(UpdateView):
    model = Musician
    form_class = MusiciansForm
    pk_url_kwarg = 'id'
    template_name = 'editMusicians.html'
    success_url = reverse_lazy("view_musics")


class RegisterUserView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy("view_musics")
    template_name = 'registerUser.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Register"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user=user)
        return response


class LogoutUserView(LogoutView):
    next_page = reverse_lazy("homePage")


class LoginUserView(LoginView):
    template_name = 'registerUser.html'
    next_page = reverse_lazy("homePage")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Login"
        return context
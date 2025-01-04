from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Car, Brand, Orders, Comment
from .forms import SignUpForm, UpdateUserForm, CommentForm
# Create your views here.


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy("homePage")
    template_name = "authForm.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Sign up'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user=user)
        return response


@method_decorator(login_required, name="dispatch")
class LogOutUserView(LogoutView):
    next_page = reverse_lazy("homePage")


class LogInUserView(LoginView):
    success_url = reverse_lazy("homePage")
    template_name = "authForm.html"
    next_page = reverse_lazy("homePage")
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Login"
        return context


@method_decorator(login_required, name="dispatch")
class UpdateUserView(UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = "authForm.html"
    success_url = reverse_lazy("profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Update'
        return context

    def get_object(self, queryset=None):
        return self.request.user


@method_decorator(login_required, name="dispatch")
class ProfileView(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logged_in_user = self.request.user
        user = User.objects.get(username=logged_in_user)
        orders = Orders.objects.filter(user=user)
        context["orders"] = orders
        return context


class HomePage(ListView):
    model = Car
    template_name = 'home.html'

    def get_queryset(self):
        q = super().get_queryset()
        brand = self.kwargs.get('brand')
        if brand is not None:
            q = Car.objects.filter(brand__id=brand)

        return q

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = context['object_list']
        context['brands'] = Brand.objects.all()
        return context


class CarDetailView(DetailView):
    model = Car
    template_name = 'carDetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = context['object']
        context['form'] = CommentForm()
        context['total_comment'] = Comment.objects.filter(
            car__id=self.kwargs.get('pk')).count()
        context['comments'] = Comment.objects.filter(
            car__id=self.kwargs.get('pk'))
        return context

    def post(self, request, *args, **kwargs):
        car_id = self.kwargs.get('pk')
        logged_in_user = self.request.user

        car = Car.objects.get(pk=car_id)
        user = User.objects.get(username=logged_in_user)

        order = Orders(user=user, car=car)
        order.save()

        car.quantity = car.quantity - 1
        car.save()

        return self.get(self.request)


def save_comments(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        car = Car.objects.get(pk=pk)
        new_cmt = Comment(
            name=form.cleaned_data['name'], body=form.cleaned_data['body'], car=car)
        new_cmt.save()
    return redirect("car_detail", pk=pk)
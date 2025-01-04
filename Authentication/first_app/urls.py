from django.urls import path
from . import views
urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('register/', views.register_user, name="register_user"),
    path('logout/', views.logout_user, name="logout_user"),
    path('login/', views.login_user, name="login_user"),
    path('profile/', views.profile, name="profile"),
    path('change-password/', views.change_password_with_old_password,
         name="change_password_with_old_password"),
    path('change-password/2/', views.change_password_without_old_password,
         name="change_password_without_old_password"),
]
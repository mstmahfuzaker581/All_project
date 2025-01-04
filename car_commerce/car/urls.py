from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePage.as_view(), name="homePage"),
    path('sign-up/', views.SignUpView.as_view(), name="sing_up"),
    path('logout/', views.LogOutUserView.as_view(), name="logout"),
    path('login/', views.LogInUserView.as_view(), name="login"),
    path('update/', views.UpdateUserView.as_view(), name="update"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('filter/<int:brand>/', views.HomePage.as_view(), name="brand_filter"),
    path('car/<int:pk>/', views.CarDetailView.as_view(), name="car_detail"),
    path('car/order/<int:pk>/', views.CarDetailView.as_view(), name="car_detail"),
    path('car/comment/<int:pk>/', views.save_comments, name="comment"),
]
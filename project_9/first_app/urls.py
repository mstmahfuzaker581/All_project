from django.urls import path,include
from . import views
#from first_app.views import home
urlpatterns = [
    path('',views.home,name="homepage"),
]

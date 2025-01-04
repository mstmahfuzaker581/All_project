
from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name="register_user"),
    path('logout/', views.LogoutUserView.as_view(), name="logout_user"),
    path('login/', views.LoginUserView.as_view(), name="login_user"),
    path('add/', views.AddMusiciansView.as_view(), name="add_musicians"),
    path('delete/album/<int:id>',
         views.DeleteAlbumView.as_view(), name="delete_album"),
    path('edit/album/<int:id>', views.UpdateAlbumView.as_view(), name="edit_album"),
    path('edit/musician/<int:id>',
         views.UpdateMusicsView.as_view(), name="edit_musician"),
    path('add/album/', views.AddAlbumView.as_view(), name="add_album"),
    path('view-musics/', views.DisplayMusicsView.as_view(), name="view_musics"),
]

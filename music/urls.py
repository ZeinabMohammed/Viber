
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
app_name="music"
urlpatterns = [
	#music/
    path('', views.IndexView.as_view(), name="index"),
    #music/71
    path('<pk>/detail', views.DetailView.as_view(), name='detail'),
  	path('album/add', views.AlbumCreate.as_view(), name="album_add"),
  	path('update/<pk>', views.AlbumUpdate.as_view(), name="album_update"),
  	path('album/<pk>/delete', views.AlbumDelete.as_view(), name="album_delete"),
 	path('album/search',views.SearchMusicView.as_view(), name='search'),

 	path('register/', views.UserFormView.as_view(), name="register"),
 	path('login/', views.login_page, name="login"),
 	path('logout/', views.logout_request, name="logout"),
]


from django.contrib import admin
from django.urls import path,include
from .import views
app_name = 'authapp'
urlpatterns = [
    path('#', views.login,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout,name='logout'),
    path('index/',views.view_user_data,name="index"),
    path('addmovie/',views.add_movie,name="add_movie"),
    path("filterdmovie/",views.filter_movies,name="filter_movies"),
    path('searchmovie/',views.movie_searcher,name='movie_searcher'),
    path('movies/<int:id>/',views.view_movie_info,name="view_movie_info"),
    path('all_movies/',views.all_movies,name="all_movies"),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path("searchmovies/",views.search_movies,name="search_movies"),




]

from django.urls import path
from movies.views import movies_list, movie_detail, movie_update, movie_add, movie_delete, movie_rate, movie_comment

urlpatterns = [
    path('', movies_list, name='movies_list'),
    path('movies/', movies_list, name='movies_list'),
    path('movies/<int:pk>/', movie_detail, name='movie_detail'),
    path('movies/add/', movie_add, name='movie_add'),
    path('movies/<int:pk>/edit/', movie_update, name='movie_update'),
    path('movies/<int:pk>/delete/', movie_delete, name='movie_delete'),
    path('movies/<int:pk>/rate', movie_rate, name='movie_rate'),
    path('movies/<int:pk>/comment', movie_comment, name='movie_comment'),
]

from django.urls import path

from movies.views import movies_list, movie_detail, movie_update, movie_add, movie_rate

urlpatterns = [
    path('', movies_list, name='movies_list'),
    path('movies/', movies_list, name='movies_list'),
    path('movies/<int:pk>/', movie_detail, name='movie_detail'),
    path('movies/add/', movie_add, name='movie_add'),
    path('movies/<int:pk>/edit/', movie_update, name='movie_update'),
    path('movies/<int:pk>/rate/', movie_rate, name='movie_rate'),
]

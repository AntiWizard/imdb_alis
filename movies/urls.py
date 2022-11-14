from django.urls import path
from movies.views import movies_list, movie_detail, movie_update, movie_add

urlpatterns = [
    path('', movies_list, name='movies_list'),
    path('movies/', movies_list, name='movies_list'),
    path('movie/<int:pk>', movie_detail, name='movie_detail'),
    path('movies/add/', movie_add, name='movie_add'),
    path('movies/<int:pk>/edit/', movie_update, name='movie_update'),
]

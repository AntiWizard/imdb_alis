from django.urls import path, include
from movies.api.views import api_root
from movies.views import movies_list, movie_detail, movie_update, movie_add, movie_rate, admin_view

urlpatterns = [
    path('api/', include('movies.api.urls')),
    path('', api_root),
    path('admin/', admin_view, name='django_admin'),
    path('movies/', movies_list, name='movies_list'),
    path('movies/<int:pk>/', movie_detail, name='movie_detail'),
    path('movies/add/', movie_add, name='movie_add'),
    path('movies/<int:pk>/edit/', movie_update, name='movie_update'),
    path('movies/<int:pk>/rate/', movie_rate, name='movie_rate'),
]

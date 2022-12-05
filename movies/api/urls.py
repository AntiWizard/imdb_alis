from django.urls import path

from movies.api.views import MovieListAPIView, MovieDetailAPIView, api_root

urlpatterns = [
    path('', api_root),
    path('movies/', MovieListAPIView.as_view(), name='movies_list_api'),
    path('movies/<int:pk>/', MovieDetailAPIView.as_view(), name='movies_detail_api'),
]

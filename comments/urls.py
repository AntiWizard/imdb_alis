from django.urls import path

from comments.views import movie_comment,parent_comment

urlpatterns = [
    path('movies/<int:movie_pk>/comment/<int:comment_pk>/add', movie_comment, name='movie_comment'),
    path('movies/<int:movie_pk>/comment/<int:comment_pk>/reply', parent_comment, name='parent_comment'),
]

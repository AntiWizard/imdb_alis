from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from movies.api.serializers import MovieSerializer
from movies.models import Movie


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'movies': reverse('movies_list', request=request, format=format)
    })


class MovieListAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.filter(is_valid=True).prefetch_related('genres', 'crew')
    serializer_class = MovieSerializer


class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.filter(is_valid=True).prefetch_related('genres', 'crew')
    serializer_class = MovieSerializer

    def perform_destroy(self, instance):
        instance.is_valid = False
        instance.save()

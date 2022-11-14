from django.shortcuts import render, get_object_or_404

from movies.models import Movie


def movies_list(request):
    movies = Movie.objects.all()[:8]
    context = {
        "movies": movies,
        "is_valid": True
    }
    return render(request, 'movies/movies_list.html', context=context)


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, "movies/movie_detail.html",
                  context={"movie": movie, "crews": movie.crew.all()})

def movie_update(request, pk):
    pass
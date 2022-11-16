from django.shortcuts import render, redirect, get_object_or_404

from movies.models import Movie
from movies.forms import MovieForm, SignUpForm

from django.contrib.auth import login
from django.http import HttpResponse

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


def movie_add(request, movie_form=None):
    if not movie_form:
        movie_form = MovieForm()
    return render(request, 'movies/movie_add.html', context={'form': movie_form})


def movie_update(request, pk, movie_form=None):
    movie = get_object_or_404(Movie, pk=pk, is_valid=True)

    if not movie_form:
        movie_form = MovieForm(instance=movie)

    context = {
        'form': movie_form,
        'movie': movie
    }
    return render(request, 'movies/movie_update.html', context=context)


def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk, is_valid=True)
    movie.is_valid = False
    movie.save()

    return redirect('movies_list')


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponse("<h2>Registration successful</h2>")
        return HttpResponse(str(form.errors))
    form = SignUpForm()
    return render(request, 'movies/sign_up.html', {"register_form": form})

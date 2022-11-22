from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from movies.forms import MovieForm
from movies.models import Movie, MovieCrew, MovieComment


def movies_list(request):
    if request.method == "GET":
        movies = Movie.objects.filter(is_valid=True)[:8]
        context = {
            "movies": movies,
        }
        return render(request, 'movies/movies_list.html', context=context)

    elif request.method == "POST":
        movie_form = MovieForm(request.POST, request.FILES)
        if not movie_form.is_valid():
            return movie_add(request, movie_form=movie_form)
        movie_form.save()
        return redirect('movies_list')


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "GET":
        context = {"movie": movie,
                   'movie_crew_list': MovieCrew.objects.filter(movie=movie)
                   .select_related('crew', 'role'),
                   'comments': MovieComment.objects.filter(movie=movie, status=MovieComment.APPROVED)
                   }
        return render(request, "movies/movie_detail.html", context=context)

    elif request.method == "POST":
        if request.POST.get('save'):
            movie_form = MovieForm(request.POST, request.FILES, instance=movie)
            if not movie_form.is_valid():
                return movie_update(request, pk, movie_form)
            movie_form.save()
            return redirect('movie_detail', pk)
        elif request.POST.get('delete'):
            return movie_delete(request, pk)


@login_required
def movie_add(request, movie_form=None):
    if not movie_form:
        movie_form = MovieForm()
    return render(request, 'movies/movie_add.html', context={'form': movie_form})


@login_required
def movie_update(request, pk, movie_form=None):
    movie = get_object_or_404(Movie, pk=pk, is_valid=True)

    if not movie_form:
        movie_form = MovieForm(instance=movie)

    context = {
        'form': movie_form,
        'movie': movie,
    }
    return render(request, 'movies/movie_update.html', context=context)


@login_required
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk, is_valid=True)
    movie.is_valid = False
    movie.save()

    return redirect('movies_list')

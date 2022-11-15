from django.shortcuts import render, get_object_or_404, redirect

from movies.forms import MovieForm, MovieCommentForm
from movies.models import Movie, Comment


def movies_list(request):
    movies = Movie.objects.filter(is_valid=True)[:8]
    context = {
        "movies": movies,
        "is_valid": True
    }
    return render(request, 'movies/movies_list.html', context=context)


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "GET":
        movie.update_view_count()
        return render(request, "movies/movie_detail.html",
                      context={"movie": movie, "crews": movie.crew.all(), "comments": movie.comment_set.all()})

    elif request.method == "POST":
        movie_form = MovieCommentForm(request.POST)
        if not movie_form.is_valid():
            return movie_comment(request, pk, movie_form=movie_form)
        Comment.objects.create(name=request.POST.get('name'), comment_text=request.POST.get('comment_text'),
                               movie_id=pk)
        return redirect("movie_detail", pk=pk)


def movie_rate(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "GET":
        return render(request, "movies/movie_rate.html",
                      context={"movie": movie})
    elif request.method == "POST":
        rate = int(request.POST.getlist('rate')[0])
        movie.update_rate(rate)
        return redirect("movies_list")


def movie_comment(request, pk, movie_form=None):
    movie = get_object_or_404(Movie, pk=pk)

    if not movie_form:
        movie_form = MovieCommentForm(instance=movie)

    return render(request, "movies/movie_comment.html",
                  context={"movie": movie, "form": movie_form})


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

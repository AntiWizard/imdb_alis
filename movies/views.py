from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from movies.models import Movie, MovieCrew, MovieComment, MovieRating
from movies.forms import MovieForm, SearchForm


def movies_list(request):
    search_form = SearchForm()
    if request.method == "GET":
        movies = Movie.objects.filter(is_valid=True)[:8]
        context = {
            "movies": movies,
            "search_form": search_form
        }
        return render(request, 'movies/movies_list.html', context=context)

    elif request.method == "POST":
        if request.POST.get('search'):
            context = {"search_form": search_form}
            s_text = request.POST.get('search_text')
            if len(s_text) >= 3:
                search_movie = Movie.objects.filter(title__icontains=request.POST.get('search_text'))
                context = {
                    "movies": search_movie,
                    "search_form": search_form
                }
            return render(request, 'movies/movies_list.html', context=context)
        else:
            movie_form = MovieForm(request.POST, request.FILES)
            if not movie_form.is_valid():
                return movie_add(request, movie_form=movie_form)
            movie_form = movie_form.save(commit=False)
            movie_form.is_valid = False
            movie_form.save()
            return redirect('movies_list')


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "GET":
        movie_crew = MovieCrew.objects.filter(movie=movie).select_related('crew', 'role')
        genres = ", ".join([item.title.title() for item in movie.genres.all()])
        crew_role = [{str(item.role): str(item.crew)} for item in movie_crew]
        actors = []
        directors = []
        for item in crew_role:
            if item.get('Actor') is not None:
                actors.append(item.get('Actor'))
            elif item.get('Director') is not None:
                directors.append(item.get('Director'))
        context = {"movie": movie,
                   "genres": genres,
                   "actors": ", ".join(actors),
                   "directors": ", ".join(directors),
                   'comments': MovieComment.objects.filter(movie=movie, status=MovieComment.APPROVED)
                   }
        return render(request, "movies/movie_detail.html", context=context)

    elif request.method == "POST":
        if request.POST.get('save'):
            movie_form = MovieForm(request.POST, request.FILES, instance=movie)
            if not movie_form.is_valid():
                return movie_update(request, pk, movie_form)
            movie_form = movie_form.save(commit=False)
            movie_form.is_valid = False
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


@login_required
def movie_rate(request, pk):
    movie = get_object_or_404(Movie, pk=pk, is_valid=True)
    if request.method == "GET":
        return render(request, 'movies/movie_rate.html', context={"movie": movie})
    elif request.method == "POST":
        MovieRating.objects.create(user=request.user, movie=movie, rate=request.POST.get("rate"))
        return redirect('movies/movie_rate.html', pk)
    return render(request, 'movies/movie_rate.html', context={"movie": movie})


def admin_view(request):
    return render(request, "admin/login.html")

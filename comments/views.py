from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from comments.forms import MovieCommentForm
from movies.models import Movie, MovieComment


@login_required
def movie_comment(request, movie_pk, comment_pk, form=None):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == "GET":
        if comment_pk == 0:
            form = MovieCommentForm()
        elif not form:
            form = MovieCommentForm(instance=movie.moviecomment_set.get(pk=comment_pk))
        return render(request, "comments/movie_comment.html",
                      context={"movie": movie, "form": form, "comment_pk": comment_pk})

    if request.method == "POST":
        if request.POST.get('edit'):
            form = MovieCommentForm(instance=movie.moviecomment_set.get(pk=comment_pk))
            return render(request, "comments/movie_comment.html",
                          context={"movie": movie, "form": form, "comment_pk": comment_pk})

        elif request.POST.get('delete'):
            movie.moviecomment_set.filter(pk=comment_pk).update(status=MovieComment.DELETED)
            return redirect('movie_detail', movie_pk)

        elif request.POST.get('reply'):
            comment = movie.moviecomment_set.get(pk=comment_pk)
            form = MovieCommentForm()
            return render(request, "comments/reply_comment.html",
                          context={"movie": movie, "form": form, "comment": comment})
        else:
            form = MovieCommentForm(request.POST)
            if not form.is_valid():
                return movie_comment(request, movie_pk, comment_pk, form)
            if comment_pk == 0:
                MovieComment.objects.create(
                    comment_body=request.POST.get("comment_body"),
                    movie=movie, user=request.user
                )
            else:
                MovieComment.objects.filter(pk=comment_pk).update(
                    movie=movie,
                    user=request.user,
                    comment_body=request.POST.get("comment_body"),
                    status=MovieComment.CREATED
                )
            return redirect('movie_detail', movie_pk)


@login_required
def parent_comment(request, movie_pk, comment_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment = get_object_or_404(MovieComment, pk=comment_pk)

    form = MovieCommentForm(request.POST)
    if not form.is_valid():
        return render(request, "comments/reply_comment.html",
                      context={"form": form, "movie": movie, "comment": comment})

    MovieComment.objects.create(movie=movie, user=request.user,
                                comment_body=request.POST.get("comment_body")
                                , parent=comment)

    return redirect('movie_detail', movie_pk)

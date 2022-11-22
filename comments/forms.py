from django import forms

from movies.models import MovieComment, CrewComment


class MovieCommentForm(forms.ModelForm):
    class Meta:
        model = MovieComment
        fields = ('comment_body',)
        widgets = {
            'comment_body': forms.Textarea(attrs={"rows": 5, "cols": 40, "placeholder": "comment"})
        }


class CrewCommentForm(forms.ModelForm):
    class Meta:
        model = CrewComment
        fields = ('comment_body',)
        widgets = {
            'comment_body': forms.Textarea(attrs={"rows": 5, "cols": 40, "placeholder": "comment"})
        }

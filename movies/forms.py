from django import forms
from django.core.exceptions import ValidationError

from movies.models import Movie, Comment


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'description', 'release_date', 'avatar',)
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }


class MovieCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'comment_text',)

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise ValidationError("Name not valid")
        return name

    def clean_comment_text(self):
        comment_text = self.cleaned_data['comment_text']
        if len(comment_text) < 10:
            raise ValidationError("Comment text must greater than 10 character")
        return comment_text

from django import forms

from movies.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'description', 'release_date', 'avatar', 'genres', 'crew')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }

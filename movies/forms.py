from django import forms

from movies.models import Movie


class MovieForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        self.fields['genres'].required = False
        self.fields['crew'].required = False

    class Meta:
        model = Movie
        fields = ('title', 'description', 'release_date', 'avatar', 'genres', 'crew')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }

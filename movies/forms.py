from django import forms

from movies.models import Movie, Genre, Crew


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


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('title',)


class CrewForm(forms.ModelForm):
    class Meta:
        model = Crew
        fields = ('first_name', 'last_name', 'birthday', 'gender', 'avatar',)


class SearchForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title',)

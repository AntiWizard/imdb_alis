from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import F


class Genre(models.Model):
    title = models.CharField(max_length=50)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Role(models.Model):
    title = models.CharField(max_length=50)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Crew(models.Model):
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, default=MALE)
    avatar = models.ImageField(upload_to='crew/avatars/', null=True, blank=True)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rate = models.FloatField(default=0)
    voter = models.PositiveIntegerField(default=0)
    view_count = models.PositiveIntegerField(default=0)
    release_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='movies/avatars/', null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    crew = models.ManyToManyField(Crew, through='MovieCrew')
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def get_description(self):
        return self.description.lower()

    # def update_rate(self, record):
    #     self.rate = ((self.rate * self.voter) + record) / (self.voter + 1)
    #     self.voter += 1
    #     self.save()

    def update_rate(self, record):
        self.rate = ((F('rate') * F('voter')) + record) / (F('voter') + 1)
        self.voter = F('voter') + 1
        self.save()
        self.refresh_from_db()

    def update_view_count(self):
        self.view_count = F('view_count') + 1
        self.save()
        self.refresh_from_db()

    def __str__(self):
        return self.title


class MovieCrew(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('movie', 'crew', 'role')


class Comment(models.Model):
    name = models.CharField(max_length=40, blank=True)
    comment_text = models.TextField(blank=True)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

from rest_framework import serializers

from movies.models import Movie, Genre, Crew, MovieCrew, Role, MovieComment, MovieRating


class MovieCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieComment
        fields = ('movie', 'user', 'parent', 'comment_body', 'status', 'validated_by', 'created_time', 'modified_time')


class MovieRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRating
        fields = ('user', 'movie', 'rate')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('title',)


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = ('first_name', 'last_name', 'gender',)


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('title',)


class MovieCrewSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    crew = CrewSerializer()

    class Meta:
        model = MovieCrew
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    movie_crew = MovieCrewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'release_date', 'avatar',
                  'created_time', 'genres', 'movie_crew')
        extra_kwargs = {'release_date': {'write_only': True}, 'avatar': {'required': False}}

    def create(self, validated_data):
        genres = validated_data.pop('genres')
        instance = Movie.objects.create(**validated_data)

        movie_genres = Genre.objects.filter(title__in=[item['title'] for item in genres])
        instance.genres.set(movie_genres)
        # [instance.genres.add(item) for item in movie_genres]
        return instance

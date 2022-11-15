from django.contrib import admin
from django.db.models import F

from movies.models import Role, Genre, Crew, MovieCrew, Movie, Comment


class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


class CrewAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'gender', 'is_valid')
    search_fields = ('first_name', 'last_name')
    list_filter = ('is_valid',)


class MovieCrewInline(admin.TabularInline):
    model = MovieCrew
    extra = 2
    readonly_fields = ('crew_gender',)

    @staticmethod
    def crew_gender(obj):
        return obj.crew.get_gender_display()


class GenreInlineAdmin(admin.StackedInline):
    model = Movie.genres.through
    extra = 3


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date', 'is_valid')
    search_fields = ('title',)
    list_filter = ('is_valid',)
    inlines = (MovieCrewInline, GenreInlineAdmin)
    exclude = ('genres',)
    actions = ['view_count_plus_ten', "change_to_valid"]

    @admin.action(description='view count plus 10')
    def view_count_plus_ten(modeladmin, request, queryset):
        queryset.update(view_count=F("view_count") + 10)

    @admin.action(description='change to valid')
    def change_to_valid(modeladmin, request, queryset):
        queryset.update(is_valid=True)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'comment_text', 'created_time', 'is_valid')
    search_fields = ("name", 'created_time', "is_valid",)


admin.site.register(Role, RoleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Crew, CrewAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment, CommentAdmin)

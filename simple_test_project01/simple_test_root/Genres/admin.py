from django.contrib import admin
from .models import Artist, Genre

class ArtistAdmin(admin.TabularInline):
    model = Artist
    extra = 1

class GenreAdmin(admin.ModelAdmin):
    inlines = [ArtistAdmin]
    
admin.site.register(Genre, GenreAdmin)


from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Artist, UserProfile

def home(request):
    return HttpResponse("Hi, this is our home page!")

class ArtistUpdate(UpdateView):
    model = Artist
    template_name = "Genres/artist_update_form.html"
    fields = ["name", "genre", "bio", "image"]

class ArtistDelete(DeleteView):
    model = Artist
    template_name = "Genres/artist_delete_form.html"
    success_url = reverse_lazy("artist_list")

class ArtistCreate(CreateView):
    model = Artist
    template_name = 'Genres/artist_create_form.html'
    fields = ["name", "genre", "bio", "image"]

class ArtistDetail(DetailView):
    model = Artist
    template_name = 'genres/artist_detail.html'

class ArtistList(ListView):
    model = Artist
    template_name = 'genres/artist_list.html'

class UserProfileUpdate(UpdateView):
    model = UserProfile
    template_name = "genres/userprofile_update_form.html"
    fields = ["bio", "profile_pic"]

class UserProfileDelete(DeleteView):
    model = UserProfile
    template_name = "genres/userprofile_delete_form.html"
    success_url = reverse_lazy("userprofile_list")

class UserProfileCreate(CreateView):
    model = UserProfile
    template_name = 'genres/userprofile_create_form.html'
    fields = ["bio", "profile_pic"]

class UserProfileDetail(DetailView):
    model = UserProfile
    template_name = 'genres/userprofile_detail.html'

class UserProfileList(ListView):
    model = UserProfile
    template_name = 'genres/userprofile_list.html'
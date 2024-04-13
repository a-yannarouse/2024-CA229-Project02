from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Genre, Artist, UserProfile
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from .contact import ContactForm
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import OrderForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


#from .filters import OrderFilter

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was create for ' + user)
            return redirect('login')
    context = {'form':form}
    return render(request, 'genres/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Genres')
        else:
            messages.info(request, 'Username OR Password is incorrect')
            
    context = {}
    return render(request, 'genres/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

class Genres(ListView):
    template_name = 'Genres/home.html'
    queryset = Genre.objects.all()
    context_object_name = 'genres'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['attractions'] = Artist.objects.all()
        return context
    
def contact(request):
	submitted = False
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			con = get_connection('django.core.mail.backends.console.EmailBackend')
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'noreply@dcu.ie'),
				['student@dcu.ie'], # change this
				connection=con
			)
			return HttpResponseRedirect('/contact?submitted=True')
	else:
		form = ContactForm()
		if 'submitted' in request.GET:
			submitted = True
	context = {
		'form': form,
		'page_list': Genre.objects.all(),
		'submitted': submitted
	}
	return render(request, 'User/contact.html', context)

class Rap(ListView):
    template_name = 'genres/rap.html'
    queryset = Genre.objects.all()
    context_object_name = 'Genres'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre = Genre.objects.get(name='Rap')
        context['genre'] = genre
        context['artists'] = Artist.objects.filter(genre=genre)
        return context

class Pop(ListView):
    template_name = 'genres/pop.html'
    queryset = Genre.objects.all()
    context_object_name = 'Genres'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre = Genre.objects.get(name='Pop')
        context['genre'] = genre
        context['artists'] = Artist.objects.filter(genre=genre)
        return context

class Country(ListView):
    template_name = 'genres/country.html'
    queryset = Genre.objects.all()
    context_object_name = 'Genres'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre = Genre.objects.get(name='Country')
        context['genre'] = genre
        context['artists'] = Artist.objects.filter(genre=genre)
        return context
    
class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'artist_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artist = self.get_object()
        youtube_channels = artist.youtubechannel_set.all()  # Access related YouTubeChannel instances
        if youtube_channels:
            # Assuming you want to display information for each YouTubeChannel
            for youtube_channel in youtube_channels:
                video_url = youtube_channel.youtube_url
                video_id = video_url.split('=')[-1]  # Extract video ID from URL
                context['youtube_video_id'] = video_id
                context['youtube_video_name'] = youtube_channel.name
        return context



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
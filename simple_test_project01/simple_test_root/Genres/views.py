from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Genre, Artist, UserProfile
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from .contact import ContactForm

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
    template_name = 'genres/artist_detail.html'

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
from django.urls import path
from . import views
from .views import ArtistDetailView

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.Genres.as_view(), name='Genres'),
    path('contact/', views.contact, name='contact'),
    path('rap/', views.Rap.as_view(), name='rap'),
    path('pop/', views.Pop.as_view(), name='pop'),
    path('country/', views.Country.as_view(), name='country'),
    path('artist/<int:pk>/', ArtistDetailView.as_view(), name='ArtistDetail'),
    path('userprofiles/', views.UserProfileList.as_view(), name='userprofile_list'),
    path("userprofile/create/", views.UserProfileCreate.as_view(), name="userprofile_create"),
    path("userprofile/<int:pk>/", views.UserProfileDetail.as_view(), name="userprofile_detail"),
    path("userprofile/update/<int:pk>/", views.UserProfileUpdate.as_view(), name="userprofile_update"),
    path("userprofile/delete/<int:pk>/", views.UserProfileDelete.as_view(), name="userprofile_delete"),
]



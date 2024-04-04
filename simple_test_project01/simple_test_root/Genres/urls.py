from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('userprofiles/', views.UserProfileList.as_view(), name='userprofile_list'),
    path("artist/create/", views.ArtistCreate.as_view(), name="artist_create"),
    path("artist/<int:pk>/", views.ArtistDetail.as_view(), name="artist_detail"),
    path("artist/update/<int:pk>/", views.ArtistUpdate.as_view(), name="artist_update"),
    path("artist/delete/<int:pk>/", views.ArtistDelete.as_view(), name="artist_delete"),
    path("userprofile/create/", views.UserProfileCreate.as_view(), name="userprofile_create"),
    path("userprofile/<int:pk>/", views.UserProfileDetail.as_view(), name="userprofile_detail"),
    path("userprofile/update/<int:pk>/", views.UserProfileUpdate.as_view(), name="userprofile_update"),
    path("userprofile/delete/<int:pk>/", views.UserProfileDelete.as_view(), name="userprofile_delete"),
    path('', views.home, name='home'),  # Assuming geography_home is replaced with index
]
from django.urls import path
from profiles import views

urlpatterns = [
    path('dj-rest-auth/registration/', CustomRegisterView.as_view(), name='custom_registration'),
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
    path('artists/', views.ArtistList.as_view()),
    path('artists/<int:pk>/', views.ArtistDetail.as_view()),
]
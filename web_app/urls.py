from django.urls import path
from . import views

urlpatterns = [

     path('',views.home,name='home' ),
     path('about/',views.about,name='about' ),
     path('rentals/',views.rentals,name='rentals' ),
     path('movies/',views.movies,name='movies' ),
     path('returns/',views.returns,name='returns'),



]
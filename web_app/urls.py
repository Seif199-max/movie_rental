from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [

     path('',views.home,name='home' ),

     path('about/',views.about,name='about' ),

     path('rentals/',views.rentals,name='rentals' ),

     path('movies/',views.movies,name='movies' ),

     path('movies_item/<int:pk>/',views.movies_item,name='movies_item' ),

     path('returns/',views.returns,name='returns'),

     path("register/", views.register, name="register"),

    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),

    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),




]
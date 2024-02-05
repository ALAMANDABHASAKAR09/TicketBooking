from django.urls import path
from .import views
from django.contrib.auth import views as ad

urlpatterns = [
    path('home/',views.homeView,name="home_url"),
    path('about/',views.about,name="about_url"),
    path('login/',ad.LoginView.as_view(template_name="html/login.html"),name="login_url"),
	path('signup/',views.signupView,name="signup_url"),
	path('logout/',ad.LogoutView.as_view(template_name="html/logout.html"),name="logout_url"),
	path('movie_list/',views.movieView,name="movie_list_url"),
	path('movie_delete/<int:y>/',views.movieDeleteView,name="movie_delete_url"),
	path('movie_update/<int:w>/',views.movieUpdateView,name="movie_update_url"),
    path('ticket_booking/',views.bookingView,name="ticket_booking_url"),
]
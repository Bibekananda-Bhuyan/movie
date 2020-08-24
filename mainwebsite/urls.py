from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="Home Page"),
    path('movie-details/<slug:id>',views.movie_details,name="Movie Details"),
    path('movie-ticket-plan/<slug:id>',views.movie_ticket_plan,name="Movie Ticket Plan"),
    path('movie-seat-plan',views.movie_seat_plan,name="Movie Seat Plan"),
    path('movie-checkout',views.movie_checkout,name="Movie Checkout"),
    path('movie-thanks',views.thanks,name="Movie Thanks"),
    path('event-details/<slug:id>',views.event_details,name="Event Details"),
    path('event-checkout/<slug:id>',views.event_checkout,name="Event Checkout"),
    path('submit-newletter',views.submit_newsletter,name="Submit News Letter"),
    path('all-movies',views.all_movies,name="All Movies"),
    path('all-events',views.all_events,name="All Events"),


    #APIS LISTS HERE
    path('api/v1/all-movies',views.get_all_movies,name="All Movies Api"),
    path('api/v1/all-events',views.get_all_events,name="All Events Api"),
    path('api/v1/single-movie-data',views.get_specific_movies,name="Single Movie Data"),
    path('api/v1/single-event-data',views.get_specific_events,name="Single Event Data"),
    path('api/v1/event-booking',views.event_booking_api,name="Event Booking Api"),
    path('api/v1/movie-booking',views.movie_booking_api,name="Movie Booking Api"),


    #CURD
    path('curd/all-movie-bookings',views.all_movie_curd_bookings,name="All Movie Bookings CURD"),
    path('curd/movie-bookings/edit/<slug:id>',views.all_movie_curd_edit_bookings,name="All Movie EDIT Bookings CURD"),
    path('curd/movie-bookings/delete/<slug:id>',views.all_movie_curd_delete_bookings,name="All Movie Delete Bookings CURD"),


]

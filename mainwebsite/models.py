from django.db import models

# Create your models here.

class Allowscreens(models.Model):
    screen_name=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.screen_name

    class Meta:
        verbose_name = "Allow Screen"

class Actors(models.Model):
    Actor_name=models.CharField(max_length=100, default="")
    Actor_photo=models.ImageField(upload_to='mainwebsite/uploadimages/actors')

    def __str__(self):
        return self.Actor_name

    class Meta:
        verbose_name = "Actor"


class Moviehalls(models.Model):
    hall_name=models.CharField(max_length=100,default="")
    hall_location=models.CharField(max_length=100,default="")
    hall_total_Screens = models.CharField(max_length=100, default="")
    hall_avaliable_screen_type = models.ManyToManyField(Allowscreens,default="")

    def __str__(self):
        return self.hall_name

    class Meta:
        verbose_name = "Movie Hall"



class Movie(models.Model):
    movie_name=models.CharField(max_length=100,default="")
    movie_language=models.CharField(max_length=100,default="")
    movie_Type = models.CharField(max_length=100, default="")
    movie_duration = models.CharField(max_length=100, default="")
    movie_likes = models.CharField(max_length=100, default="")
    movie_Audience_score = models.CharField(max_length=100, default="")
    movie_Rattings = models.CharField(max_length=100, default="")
    movie_screen_type=models.ForeignKey(Allowscreens,default="",on_delete=models.CASCADE)
    movie_summery=models.TextField(max_length=100000,default="")
    movie_Actors = models.ManyToManyField(Actors, default="")
    movie_relase_hall = models.ManyToManyField(Moviehalls, default="")
    movie_thumbnil = models.ImageField(upload_to='mainwebsite/uploadimages/movies/thumbnil', default="")
    movie_big_banner = models.ImageField(upload_to='mainwebsite/uploadimages/movies/banner', default="")
    movie_photo1 = models.ImageField(upload_to='mainwebsite/uploadimages/movies/photos', default="")
    movie_photo2 = models.ImageField(upload_to='mainwebsite/uploadimages/movies/photos', default="")
    movie_photo3 = models.ImageField(upload_to='mainwebsite/uploadimages/movies/photos', default="")

    def __str__(self):
        return self.movie_name

    class Meta:
        verbose_name = "Movie"


class Event(models.Model):
    Event_name=models.CharField(max_length=100, default="")
    Event_date=models.DateField(default="")
    Event_address=models.CharField(max_length=100, default="")
    Event_email = models.CharField(max_length=100, default="")
    Event_summery = models.TextField(max_length=100000, default="")
    Event_thumbnil = models.ImageField(upload_to='mainwebsite/uploadimages/event/thumbnil', default="")
    Event_big_banner = models.ImageField(upload_to='mainwebsite/uploadimages/event/banner', default="")

    def __str__(self):
        return self.Event_name

    class Meta:
        verbose_name = "Event"

class Seatbookedformovie(models.Model):
    selected_movie=models.ForeignKey(Movie,on_delete=models.CASCADE,default="")
    selected_movie_hall=models.ForeignKey(Moviehalls,on_delete=models.CASCADE,default="")
    for_timeslots=models.CharField(max_length=100, default="")
    seat_no=models.CharField(max_length=100, default="")
    booked_time=models.DateTimeField(auto_now_add=True)

class Users(models.Model):
    user_name=models.CharField(max_length=100, default="")
    user_phone_no=models.CharField(max_length=100, default="")
    user_emailid=models.CharField(max_length=100, default="")
    created_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "User"

    def __str__(self):
        return self.user_name

class Movie_booked_by_user(models.Model):
    User=models.ForeignKey(Users,default="",on_delete=models.CASCADE)
    Selected_movie=models.ForeignKey(Movie,default="", on_delete=models.CASCADE)
    Selected_hall=models.ForeignKey(Moviehalls,default="",on_delete=models.CASCADE)
    Order_id=models.CharField(max_length=100, default="")
    user_name=models.CharField(max_length=100, default="")
    user_phone_no=models.CharField(max_length=100, default="")
    user_email=models.CharField(max_length=100, default="")
    Time_slot=models.CharField(max_length=100, default="")
    Each_ticke_tprice=models.CharField(max_length=100, default="")
    Total_ticket_price=models.CharField(max_length=100, default="")
    Total_seats=models.CharField(max_length=100, default="")
    Seat_numbers=models.CharField(max_length=100, default="")
    Booeked_time=models.DateTimeField(auto_now_add=True)
    Is_user_visited=models.BooleanField("Is User Visited Movie",default=False)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "Movie Booked By User"



class Event_booked_by_user(models.Model):
    User=models.ForeignKey(Users,default="",on_delete=models.CASCADE)
    Selected_Event = models.ForeignKey(Event, default="", on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100, default="")
    user_phone_no = models.CharField(max_length=100, default="")
    user_email = models.CharField(max_length=100, default="")
    Order_id = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "Event Booked By User"


class News_letter(models.Model):
    email=models.CharField(max_length=100, default="")
    date_creattion=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "News Letter"


from rest_framework import serializers
from .models import *

class Allowscreensserilazers(serializers.ModelSerializer):
    class Meta:
        model=Allowscreens
        fields= "__all__"

class Actorsserilazers(serializers.ModelSerializer):
    class Meta:
        model=Actors
        fields= "__all__"


class MoviehallsSerial(serializers.ModelSerializer):
    class Meta:
        model=Moviehalls
        fields="__all__"

class Movieserial(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields="__all__"

class Eventserial(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields="__all__"

class Usersserial(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields="__all__"


class Movie_booked_by_userserial(serializers.ModelSerializer):
    class Meta:
        model = Movie_booked_by_user
        fields = "__all__"

class Event_booked_by_userserial(serializers.ModelSerializer):
    class Meta:
        model = Event_booked_by_user
        fields = "__all__"


class News_letterserial(serializers.ModelSerializer):
    class Meta:
        model = News_letter
        fields = "__all__"

 


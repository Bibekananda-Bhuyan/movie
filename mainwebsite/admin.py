from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Moviehalls)
admin.site.register(Allowscreens)
admin.site.register(Actors)
admin.site.register(Movie)
admin.site.register(Event)

admin.site.register(Users)
admin.site.register(Movie_booked_by_user)
admin.site.register(Event_booked_by_user)
admin.site.register(News_letter)

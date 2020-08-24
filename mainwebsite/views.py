from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import *
import random
from django.contrib import messages
from .apis import *
# Create your views here.


def index(request):
    all_movies=Movie.objects.all()
    all_events = Event.objects.all()
    params={"movies":all_movies,"events":all_events}
    return render(request,"mainwebsite/index.html",params)



def all_events(request):

    all_events = Event.objects.all()
    params={"events":all_events}
    return render(request,"mainwebsite/events.html",params)



def all_movies(request):
    all_movies = Movie.objects.all()

    params = {"movies": all_movies}
    return render(request, "mainwebsite/movies.html", params)



def movie_details(request,id):
    try:
        cmovie=Movie.objects.get(id=id)
        params={"movie":cmovie}
    except:
        return redirect('/')

    return render(request,"mainwebsite/movie-details.html",params)


def movie_ticket_plan(request,id):
    if request.method=="POST":
        htime=request.POST.get("htime")
        mname = request.POST.get("mname")
        htime=htime.split('-')

        hallid=htime[0]
        halltime=htime[1]
        request.session["hallid"] = hallid
        request.session["movieid"] = id
        request.session["halltime"] = halltime
        request.session["mname"] = mname
        return redirect('/movie-seat-plan')

    try:
        cmovie=Movie.objects.get(id=id)
        params={"movie":cmovie}
    except:
        return redirect('/')

    return render(request,"mainwebsite/movie-ticket-plan.html",params)


def movie_seat_plan(request):
    if request.method == "POST":
        sits = request.POST.getlist('htime')
        totalsits = len(sits)
        sitprice = 300
        totalbookingprice = sitprice * totalsits
        request.session["totalsits"] = totalsits
        request.session["sitprice"] = sitprice
        request.session["totalbookingprice"] = totalbookingprice
        request.session["sits"] = sits
        return redirect('/movie-checkout')

    Selected_movie = Movie.objects.get(id=request.session["movieid"])
    Selected_hall = Moviehalls.objects.get(id=request.session["hallid"])
    bookeddata=Seatbookedformovie.objects.filter(selected_movie=Selected_movie,selected_movie_hall=Selected_hall,
                                                 for_timeslots=request.session["halltime"])

    params={"moviebookedt":bookeddata}

    return render(request, "mainwebsite/movie-seat-plan.html",params)


def movie_checkout(request):
    if request.method=="POST":
        userfname=request.POST.get("fname")
        userlname = request.POST.get("userlname")
        userphoneno = request.POST.get("userphoneno")
        useremail = request.POST.get("useremail")

        if(len(userphoneno)==10):

            check = Users.objects.filter(user_phone_no=userphoneno).count()
            if check==0:
                #This User Coming First Time For booking
                savedata=Users(user_name=userfname+userlname,user_phone_no=userphoneno,user_emailid=useremail)
                savedata.save()
                getuserid=Users.objects.get(user_phone_no=userphoneno)

            else:
                #This User Is Your Exsting User
                getuserid = Users.objects.get(user_phone_no=userphoneno)



            Selected_movie=Movie.objects.get(id=request.session["movieid"])
            Selected_hall=Moviehalls.objects.get(id=request.session["hallid"])

            finalsits = ""
            counter = 0
            for i in request.session["sits"]:
                if counter == 0:
                    finalsits = i
                    save_s_date = Seatbookedformovie(selected_movie=Selected_movie, selected_movie_hall=Selected_hall,
                                                     for_timeslots=request.session["halltime"],
                                                     seat_no=i)
                    save_s_date.save()
                else:
                    finalsits = finalsits + "," + i
                    save_s_date = Seatbookedformovie(selected_movie=Selected_movie,selected_movie_hall=Selected_hall,
                                                     for_timeslots=request.session["halltime"],
                                                     seat_no=i)
                    save_s_date.save()
                counter = counter + 1

            myoid=random.randint(10000, 10000000)
            movie_save_date=Movie_booked_by_user(User=getuserid,Selected_movie=Selected_movie,Selected_hall=Selected_hall
                                                 ,Order_id=myoid,Time_slot=request.session["halltime"],
                                                 Each_ticke_tprice=request.session["sitprice"],
                                                 Total_ticket_price=request.session["totalbookingprice"],
                                                 Total_seats=request.session["totalsits"],
                                                 Seat_numbers=finalsits,user_name=userfname+userlname,user_phone_no=userphoneno,
                                                 user_email=useremail)
            movie_save_date.save()
            request.session["bookingid"] = myoid
            return redirect('/movie-thanks')
        else:
            messages.add_message(request, messages.INFO, "You have entred invalid Phonenumber")



    selectedhall=Moviehalls.objects.get(id=request.session["hallid"])
    parms={"selectedhall":selectedhall}
    return render(request, "mainwebsite/movie-checkout.html",parms)



def thanks(request):
    return render(request,"mainwebsite/thanks.html")


def event_details(request,id):
    try:
        cmovie=Event.objects.get(id=id)
        params={"event":cmovie}
    except:
        return redirect('/')

    return render(request,"mainwebsite/event-details.html",params)


def event_checkout(request,id):
    if request.method == "POST":
        userfname = request.POST.get("fname")

        userphoneno = request.POST.get("userphoneno")
        useremail = request.POST.get("useremail")

        if (len(userphoneno) == 10):

            check = Users.objects.filter(user_phone_no=userphoneno).count()
            if check == 0:
                # This User Coming First Time For booking
                savedata = Users(user_name=userfname , user_phone_no=userphoneno, user_emailid=useremail)
                savedata.save()
                getuserid = Users.objects.get(user_phone_no=userphoneno)

            else:
                # This User Is Your Exsting User
                getuserid = Users.objects.get(user_phone_no=userphoneno)
            myoid = random.randint(10000, 10000000)
            Selected_event = Event.objects.get(id=id)

            savedata=Event_booked_by_user(User=getuserid,user_name=userfname,user_phone_no=userphoneno,
                                                 user_email=useremail,Selected_Event=Selected_event,Order_id=myoid)
            savedata.save()
            request.session["bookingid"] = myoid
            return redirect('/movie-thanks')

        else:
            messages.add_message(request, messages.INFO, "You have entred invalid Phonenumber")

    try:
        cmovie=Event.objects.get(id=id)
        params={"event":cmovie}
    except:
        return redirect('/')

    return render(request,"mainwebsite/event-checkout.html",params)


def submit_newsletter(request):
    if request.method=="POST":
        email=request.POST.get("email")
        savedate=News_letter(email=email)
        savedate.save()
        return render(request, "mainwebsite/news.html")
    if request.method=="GET":
        return redirect('/')

def all_movie_curd_bookings(request):
    movieb = Movie_booked_by_user.objects.all()
    return render(request, "mainwebsite/show.html", {'moviebs': movieb})

def all_movie_curd_edit_bookings(request,id):
    if request.method=="POST":
        orderid = request.POST.get("orderid")
        username = request.POST.get("username")
        userphoneo = request.POST.get("userphoneo")
        movieb = Movie_booked_by_user.objects.get(id=id)
        movieb.Order_id=orderid
        movieb.user_name=username
        movieb.user_phone_no=userphoneo
        movieb.save()
        return redirect('/curd/all-movie-bookings')

    try:
        movieb = Movie_booked_by_user.objects.filter(id=id)
        return render(request, "mainwebsite/edit.html", {'moviebs': movieb})
    except:
        return redirect('/curd/all-movie-bookings')

def all_movie_curd_delete_bookings(request,id):

    try:
        movieb = Movie_booked_by_user.objects.get(id=id)
        movieb.delete()
        return redirect('/curd/all-movie-bookings')
    except:
        return redirect('/curd/all-movie-bookings')


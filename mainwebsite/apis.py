from django.shortcuts import render
from django.shortcuts import render
from  rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
import random
import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_movies(request):
    queryset = Movie.objects.all()
    serializer = Movieserial(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_events(request):
    queryset = Event.objects.all()
    serializer = Eventserial(queryset, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def get_specific_movies(request):
    data = JSONParser().parse(request)
    apiresponse = {}
    if ("Movie_ID" in data and data['Movie_ID'] != ""):
        try:
            queryset = Movie.objects.filter(id=data['Movie_ID'])
            serializer = Movieserial(queryset, many=True)
            return Response(serializer.data)
        except:
            apiresponse['status'] = 702
            apiresponse['message'] = "Invalid Movie Id"
            return Response(apiresponse)
    else:
        apiresponse['status'] = 702
        apiresponse['message'] = "Invalid Movie Id"
        return Response(apiresponse)



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def get_specific_events(request):
    data = JSONParser().parse(request)
    apiresponse = {}
    if ("Event_ID" in data and data['Event_ID'] != ""):
        try:
            queryset = Event.objects.filter(id=data['Event_ID'])
            serializer = Eventserial(queryset, many=True)
            return Response(serializer.data)
        except:
            apiresponse['status'] = 702
            apiresponse['message'] = "Invalid Event Id"
            return Response(apiresponse)
    else:
        apiresponse['status'] = 702
        apiresponse['message'] = "Invalid Event Id"
        return Response(apiresponse)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def event_booking_api(request):
    data = JSONParser().parse(request)
    apiresponse = {}
    valid=0
    if ("Username" in data and data['Username'] != ""):
        if ("Useremail" in data and data['Useremail'] != ""):
            if ("userphoneno" in data and data['userphoneno'] != ""):
                if(len(data['userphoneno'])==10):
                    if ("Eventid" in data and data['Eventid'] != ""):
                        try:
                            Selected_event = Event.objects.get(id=data['Eventid'])
                            valid=1
                        except:
                            apiresponse['status'] = 711
                            apiresponse['message'] = "Invalid Event Id"
                            return Response(apiresponse)
                        if(valid==1):
                            check = Users.objects.filter(user_phone_no=data['userphoneno']).count()
                            if check == 0:
                                # This User Coming First Time For booking
                                savedata = Users(user_name=data['Username'], user_phone_no=data['userphoneno'], user_emailid=data['Username'])
                                savedata.save()
                                getuserid = Users.objects.get(user_phone_no=data['userphoneno'])

                            else:
                                # This User Is Your Exsting User
                                getuserid = Users.objects.get(user_phone_no=data['userphoneno'])
                            myoid = random.randint(10000, 10000000)
                            Selected_event = Event.objects.get(id=data['Eventid'])

                            savedata = Event_booked_by_user(User=getuserid, user_name=data['Username'], user_phone_no=data['userphoneno'],
                                                            user_email=data['Useremail'], Selected_Event=Selected_event,
                                                            Order_id=myoid)
                            savedata.save()

                            apiresponse['status'] = 712
                            apiresponse['bookingid'] = myoid
                            apiresponse['message'] = "Booking Completed"
                            return Response(apiresponse)
                        else:
                            apiresponse['status'] = 711
                            apiresponse['message'] = "Invalid Event Id"
                            return Response(apiresponse)

                    else:
                        apiresponse['status'] = 711
                        apiresponse['message'] = "Invalid Event Id"
                        return Response(apiresponse)
                else:
                    apiresponse['status'] = 710
                    apiresponse['message'] = "Invalid User Phone Number"
                    return Response(apiresponse)
            else:
                apiresponse['status'] = 707
                apiresponse['message'] = "User Phoneno Missing"
                return Response(apiresponse)
        else:
            apiresponse['status'] = 705
            apiresponse['message'] = "User Email Missing"
            return Response(apiresponse)
    else:
        apiresponse['status'] = 702
        apiresponse['message'] = "User Name Missing"
        return Response(apiresponse)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def movie_booking_api(request):
    data = JSONParser().parse(request)
    apiresponse = {}
    valid = 0
    if ("Username" in data and data['Username'] != ""):
        if ("Useremail" in data and data['Useremail'] != ""):
            if ("userphoneno" in data and data['userphoneno'] != ""):
                if (len(data['userphoneno']) == 10):
                    if ("movieid" in data and data['movieid'] != ""):
                        try:
                            Selected_movie = Movie.objects.get(id=data['movieid'])
                            valid = 1
                        except:
                            apiresponse['status'] = 711
                            apiresponse['message'] = "Invalid movie Id"
                            return Response(apiresponse)

                        if ("Selected_hall" in data and data['Selected_hall'] != ""):
                            if ("booked_Seat_list" in data and data['booked_Seat_list'] != ""):
                                if ("booked_show_time" in data and data['booked_show_time'] != ""):
                                    if ("each_ticket_price" in data and data['each_ticket_price'] != ""):
                                        if ("Total_ticket_price" in data and data['Total_ticket_price'] != ""):
                                            if ("Total_seats" in data and data['Total_seats'] != ""):

                                                check = Users.objects.filter(user_phone_no=data['userphoneno']).count()
                                                if check == 0:
                                                    # This User Coming First Time For booking
                                                    savedata = Users(user_name=data['Username'],
                                                                     user_phone_no=data['userphoneno'],
                                                                     user_emailid=data['Useremail'])
                                                    savedata.save()
                                                    getuserid = Users.objects.get(user_phone_no=data['userphoneno'])

                                                else:
                                                    # This User Is Your Exsting User
                                                    getuserid = Users.objects.get(user_phone_no=data['userphoneno'])

                                                Selected_movie = Movie.objects.get(id=data['movieid'])
                                                Selected_hall = Moviehalls.objects.get(id=data['Selected_hall'])

                                                finalsits = ""
                                                counter = 0
                                                for i in data['booked_Seat_list']:
                                                    if counter == 0:
                                                        finalsits = i
                                                        save_s_date = Seatbookedformovie(selected_movie=Selected_movie,
                                                                                         selected_movie_hall=Selected_hall,
                                                                                         for_timeslots=data['booked_show_time'],
                                                                                         seat_no=i)
                                                        save_s_date.save()
                                                    else:
                                                        finalsits = finalsits + "," + i
                                                        save_s_date = Seatbookedformovie(selected_movie=Selected_movie,
                                                                                         selected_movie_hall=Selected_hall,
                                                                                         for_timeslots=data['booked_show_time'],
                                                                                         seat_no=i)
                                                        save_s_date.save()
                                                    counter = counter + 1

                                                myoid = random.randint(10000, 10000000)
                                                movie_save_date = Movie_booked_by_user(User=getuserid,
                                                                                       Selected_movie=Selected_movie,
                                                                                       Selected_hall=Selected_hall
                                                                                       , Order_id=myoid,
                                                                                       Time_slot=data['booked_show_time'],
                                                                                       Each_ticke_tprice=data['each_ticket_price'],
                                                                                       Total_ticket_price=data['Total_ticket_price'],
                                                                                       Total_seats=data['Total_seats'],
                                                                                       Seat_numbers=finalsits,
                                                                                       user_name=data['Username'],
                                                                                       user_phone_no=data[
                                                                                           'userphoneno'],
                                                                                       user_email=data['Useremail'])
                                                movie_save_date.save()

                                                apiresponse['status'] = 750
                                                apiresponse['bookingid'] = myoid
                                                apiresponse['message'] = "Booking Completed"
                                                return Response(apiresponse)



                                            else:
                                                apiresponse['status'] = 720
                                                apiresponse['message'] = "Invalid Total Seat"
                                                return Response(apiresponse)
                                        else:
                                            apiresponse['status'] = 719
                                            apiresponse['message'] = "Invalid Total Ticket Price"
                                            return Response(apiresponse)

                                    else:
                                        apiresponse['status'] = 718
                                        apiresponse['message'] = "Invalid Single Ticket Price"
                                        return Response(apiresponse)
                                else:
                                    apiresponse['status'] = 717
                                    apiresponse['message'] = "Invalid Movie Show Time"
                                    return Response(apiresponse)
                            else:
                                apiresponse['status'] = 716
                                apiresponse['message'] = "Invalid Selected Seat List"
                                return Response(apiresponse)
                        else:
                            apiresponse['status'] = 715
                            apiresponse['message'] = "Invalid Selected_hall Id"
                            return Response(apiresponse)
                    else:
                        apiresponse['status'] = 711
                        apiresponse['message'] = "Invalid Movie Id"
                        return Response(apiresponse)
                else:
                    apiresponse['status'] = 710
                    apiresponse['message'] = "Invalid User Phone Number"
                    return Response(apiresponse)
            else:
                apiresponse['status'] = 707
                apiresponse['message'] = "User Phoneno Missing"
                return Response(apiresponse)
        else:
            apiresponse['status'] = 705
            apiresponse['message'] = "User Email Missing"
            return Response(apiresponse)
    else:
        apiresponse['status'] = 702
        apiresponse['message'] = "User Name Missing"
        return Response(apiresponse)


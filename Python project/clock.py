from datetime import datetime
import speech_recog as sp
import pytz

place_list = []
for i in pytz.all_timezones:
    if '/' in i:
        place = i.split('/')
        place_list.append(place[1])
    else:
        place_list.append(i)



def ask():
    
    sp.assistant_response("Which place?")
    try:
        place = sp.input_command().capitalize()
        if place == "Coordinated universal time":
            final = "UTC"
        else:
            try:
                final = pytz.all_timezones[place_list.index(place)]
            except ValueError:
                sp.assistant_response("The timezone requested is not available, please try again")
                ask()
        print(final)
        return final
    except AttributeError:
        sp.assistant_response("Didn't catch that, please try again")
        ask()

def world_clock():
    try:
        place_object = pytz.timezone(ask())
        place_time = datetime.now(place_object)
        result = place_time.strftime("%H:%M")
        return result
    except pytz.UnknownTimeZoneError:
        sp.assistant_response("The given timezone is incorrect, please try again")
        world_clock()

def time_now():
    right_now = datetime.now()
    result = right_now.strftime("%H:%M")
    return result






import speech_recog as sp
import time
import whatsapp as wt
import googlesrc
import translate
import clock
import yt

#list of acceptable requests
#----------------------------------------------------------------------------
def list_requests():
    print('Available requests: ')
    print("send a whatsapp message")
    print('send a scheduled whatsapp message')
    print('search the internet')
    print('translate something')
    print("what is the time right now")
    print("time for a specific place")
    print("play music")
    print("play youtube video")
    print()
#----------------------------------------------------------------------------

def RunApp():

    list_requests()
    print('Speak now .....')
    request = sp.input_command()

    #Sending a message on Whatsapp
    if request == "send a whatsapp message":
        send = wt.Whatsapp()
        if send.Instant_Message() == 0:
            sp.assistant_response('Would you like to add the contact')
            resp = sp.input_command()
            if resp == 'yes':
                send.contact_not_present()
                sp.assistant_response('Would you like to send a message to them?')
                resp_new = sp.input_command()
                if resp_new == 'yes':
                    send.Instant_Message()

    elif request == 'send a scheduled whatsapp message':
        send = wt.Whatsapp()
        if send.send_message() == 0:
            sp.assistant_response('Would you like to add the contact')
            resp = sp.input_command()
            if resp == 'yes':
                send.contact_not_present()
                sp.assistant_response('Would you like to send a message to them?')
                resp_new = sp.input_command()
                if resp_new == 'yes':
                    send.send_message()
    
    #search the net
    elif request == 'search the internet':
        googlesrc.option()

    #translation 
    elif request == 'translate something':
        translate.get_audio()

    #get current time
    elif request == "what is the time right now":
        sp.assistant_response("Please keep in mind that the time will be in 24 hour clock format")
        current = clock.time_now()
        print(current)
        sp.assistant_response(current)

    #get time for a specific place
    elif request == "time for a specific place":
        sp.assistant_response("Please keep in mind that the time will be in 24 hour clock format")
        current = clock.world_clock()
        print(current)
        sp.assistant_response(current)

    #play some music
    elif request == "play music":
        yt.music_on_yt()

    #watch a video
    elif request == "play youtube video":
        yt.video_on_yt()

    elif request == "thank you that will be all":
        sp.assistant_response("Have a great day!")
        exit()

    elif request == None:
        time.sleep(10)

    #invalid response
    else:
        sp.assistant_response("Invalid request, please try again")

sp.assistant_response('Your wish is my command')   
while True:
    RunApp()

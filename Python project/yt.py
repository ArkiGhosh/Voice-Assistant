import allwebfunc as awb
import speech_recog as sp
import time
import pywhatkit as wt

def gotovid(vid_name):
    youtube = awb.Webfunc()
    youtube.get_site("https://www.youtube.com/")
    youtube.send_data(vid_name, 'search')
    youtube.search_click("search-icon-legacy")
    #youtube.imp_wait(10)
    
def video_on_yt():
    sp.assistant_response("Which video would you like to watch?")
    resp = sp.input_command()
    gotovid(resp)
    time.sleep(10)

#things to work on:
#how to click on the youtube video after searching (current problem -> element not found, other method returns list of web elements which are sorted in alphabetical order, producing the wrong result)

#youtube music
def music_on_yt():
    sp.assistant_response("Which song would you like to listen to?")
    resp = sp.input_command()
    sp.assistant_response("Playing " + resp)
    wt.playonyt(resp)


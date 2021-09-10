#module for google search
import googlesearch as gs
from pyttsx3 import init
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import speech_recog as sp
import wikipedia as wk
import translate
import allwebfunc as awb

#google search anything and click on the first result
#----------------------------------------------------------------------------
def src(query):         #returns an iterator of results
    main_itr = gs.search(query, tld = 'com', lang = 'en', num = 10, start = 0, stop = 1, pause = 2)
    return main_itr

#----------------------------------------------------------------------------

#main function to look up stuff
#----------------------------------------------------------------------------
def look_up(a, duration):
    iter = src(a)
    for i in iter:
        result = i
        break
    Webget = awb.Webfunc()
    Webget.get_site(result)
    time.sleep(int(duration))

#----------------------------------------------------------------------------

#To get wiki results
#----------------------------------------------------------------------------
class wiki:
    def __init__(self):
        pass

    def wiki_summary(self, key, num_sentences):             #takes the keyword and the number of sentences you want to get
        result = wk.summary(key, sentences = num_sentences)
        return result

    def lang_func(self, lang):
        lang_dict = {
            'hindi' : 'hi',
            'english' : 'en',
            'bengali' : 'bn',
            'spanish' : 'es',
            'german' : 'de',
            'french' : 'fr',
            'japanese' : 'ja',
        }
        return lang_dict[lang]

    def wikinew(self, key, length):
        result = wk.page(key, auto_suggest = False).summary
        result = result.split('.')
        final = ""
        for i in range(length):
            final = final + result[i] + '.'
        return final

#----------------------------------------------------------------------------

def option():
    sp.assistant_response("Do you want a website or information about something?")
    response = sp.input_command()

    if response == "website":
        sp.assistant_response("Ok, please provide the keyword for the website")
        keyword = sp.input_command()
        sp.assistant_response("For how long do you want the website to be displayed?")
        dur = int(sp.input_command())
        look_up(keyword, dur)

    elif response == "information":
        wiki_object = wiki()
        sp.assistant_response('What do you want information about?')
        keyword = sp.input_command()
        sp.assistant_response("How long do you want your summary to be?")
        length = int(sp.input_command())
        sp.assistant_response('In what language do you want the summary?')
        sp.assistant_response("The available options are: Hindi, English, Bengali, Spanish, German, French and Japanese")
        lingo = sp.input_command()
        info = wiki_object.wikinew(keyword, length)
        #info = wiki_object.wiki_summary(keyword, length)
        translation = translate.translate_func(info, initial = 'en', final = wiki_object.lang_func(lingo))
        #print(translation)
        audio_name = translate.diff_lang_audio(translation, wiki_object.lang_func(lingo))
        time.sleep(translate.duration(audio_name) + 1)

        #will delete the file only if the entire audio is allowed to be played
        translate.delete_file(audio_name)

    else:
        sp.assistant_response("Sorry, your response is invalid, please try again")
        option()

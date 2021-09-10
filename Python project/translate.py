from gtts import gTTS
from googletrans import Translator, constants
import time
import mutagen
from mutagen.mp3 import MP3
import os

from pyttsx3 import init
import speech_recog as sp

translator = Translator()

lang_dict1 = {
            'hindi' : 'hi-IN',
            'english' : 'en-IN',
            'bengali' : 'bn-IN',
            'spanish' : 'es_ES',
            'german' : 'de-DE',
            'french' : 'fr-BE',
            'japanese' : 'ja-JP',
        }

def translate_func(txt, initial, final):
    translation = translator.translate(txt, src = initial, dest = final)
    print(translation.text)
    return translation.text

def diff_lang_audio(content, lingo):
    aud = gTTS(text = content, slow = False, lang = lingo)
    name = 'translation_audio.mp3'
    aud.save(name)
    os.system("start " + name)
    return name

def duration(name):
    t = MP3(name)
    t_info = t.info
    dur = int(t_info.length)
    return dur

def delete_file(name):
    os.remove(name)

def language_code(response):
    try:
        initial = lang_dict1[response]
        return initial 
    except KeyError:
        sp.assistant_response("Sorry, this language is not available, please try some other language.")
        get_audio()

def get_audio():
    sp.assistant_response("Ok, do you want me to translate a text or speech?")
    answer = sp.input_command()
    if answer == 'speech':
        sp.assistant_response("Which language will the speech be in")
        resp1 = sp.input_command()
        initial = language_code(resp1)
        sp.assistant_response("Ok, please speak now")
        raw_speech = sp.input_command(initial)

        #translation
        sp.assistant_response("In which language do you want the translation?")
        resp2 = sp.input_command()
        final = language_code(resp2)
        translated_speech = translate_func(raw_speech, initial[0:2], final[0:2])
        print(translated_speech)
        audio_name = diff_lang_audio(translated_speech, final[0:2])
        time.sleep(duration(audio_name) + 1)

        #will delete the file only if the entire audio is allowed to be played
        delete_file(audio_name)

    elif answer == 'text':
        sp.assistant_response("Which language will the text be in")
        resp1 = sp.input_command()
        initial = language_code(resp1)
        sp.assistant_response("Ok, please write now")
        raw_text = input()

        #translation
        sp.assistant_response("In which language do you want the translation?")
        resp2 = sp.input_command()
        final = language_code(resp2)
        translated_speech = translate_func(raw_text, initial[0:2], final[0:2])
        print(translated_speech)
        audio_name = diff_lang_audio(translated_speech, final[0:2])
        time.sleep(duration(audio_name) + 1)

        #will delete the file only if the entire audio is allowed to be played
        delete_file(audio_name)

    else:
        sp.assistant_response("Sorry, invalid response, please try again")
        get_audio()
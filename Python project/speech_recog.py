import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def input_command(lang = 'en-IN'):
    assistant_ear = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            assistant_ear.adjust_for_ambient_noise(source, duration = 1)
            voice = assistant_ear.listen(source)
            request = assistant_ear.recognize_google(voice, language = lang)
            request = request.lower()
            print(request)
        return request
    except:
        return None
    

def assistant_response(response):
    engine.say(response)
    engine.runAndWait()



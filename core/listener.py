import speech_recognition as sr
from . import speaker
from config import config

recognizer = sr.Recognizer()



def listen():
    with sr.Microphone() as source:
        if config.Listenkey:
            config.Listenkey = False
            speaker.speak("Genisys is ready to chat")
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, )
            text = recognizer.recognize_google(audio)
            return True,text.lower()
        except sr.UnknownValueError:
            return False,"Sorry, I didn't understand that."
        except sr.RequestError:
            return False,"Speech recognition service is unavailable."


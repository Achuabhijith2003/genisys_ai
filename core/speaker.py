import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Try to find an Indian-English voice
    for voice in voices:
        if 'india' in voice.name.lower() or 'indian' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break  
    
    # Reduce speaking speed
    engine.setProperty('rate', 170)  # Default is ~200, lower = slower

    engine.say(text)
    engine.runAndWait()


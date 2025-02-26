import pyttsx3

class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 170)  # Adjust speech speed

        voices = self.engine.getProperty('voices')

        # Try to find an Indian-English voice
        for voice in voices:
            if 'india' in voice.name.lower() or 'indian' in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


speaker = Speaker()


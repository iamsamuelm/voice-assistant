import pyttsx3
import speech_recognition as sr

# Friday's voice
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[82].id)
    engine.setProperty('rate', 187) 
    engine.say(text)
    engine.runAndWait()

# Understanding user commands
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print('Recognising')
        query = r.recognize_vosk(audio, laguage='en-us')
        print(f"User said: {query}")
    except Exception as e:
        return ""
    return query.lower()

text = takeCommand()
speak(text)
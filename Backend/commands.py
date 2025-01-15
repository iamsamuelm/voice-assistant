import pyttsx3

# def speak(text):
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices') 
#     print(voices)
#     engine.say(text)
#     engine.runAndWait()

# speak("Hello everyone")

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    engine.setProperty('voice', voice.id)
    print(f"Voice: {voice.name}, {voice.id}")
    engine.say("Hello, this is a sample of my voice.")
    engine.runAndWait()
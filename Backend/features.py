import os
from playsound import playsound

# Friday start sound
def playStartSound():
    # Dynamically resolve the absolute path to the sound file
    sound_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),  # Directory of features.py
        "../Frontend/assets/audio/soft-startup-sound.mp3"
    )
    playsound(sound_path)
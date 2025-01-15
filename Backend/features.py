import eel
from pydub import AudioSegment
from pydub.playback import play

# Friday's Startup Sound
@eel.expose
def playDigitalClick():
    music_dir = "/Users/semasmuma/Desktop/Portfolio/Voice Assistant/voice-assistant/Frontend/assets/audio/ui-digital-click.wav"
    sound = AudioSegment.from_wav(music_dir)
    play(sound)
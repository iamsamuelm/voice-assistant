from pydub import AudioSegment
from pydub.playback import play
import eel

#Friday start sound
@eel.expose
def playStartSound():
    sound_path = "Frontend/assets/audio/soft-startup-sound.mp3"
    sound = AudioSegment.from_file(sound_path, format="mp3")
    play(sound)
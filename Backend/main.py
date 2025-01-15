import os
import eel
from features import *

eel.init("Backend")
os.system('open -a safari http://127.0.0.1:5500/Frontend/index.html')
eel.sleep(0.1)
playDigitalClick()()
eel.start('index.html', mode=None, host='localhost', block=True)

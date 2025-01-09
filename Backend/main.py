import os
import eel
import subprocess

eel.init("Frontend")

subprocess.Popen(['open', '-a', 'Safari', 'http://localhost:8000/index.html'])

eel.start('index.html', mode=None, host='localhost', block=True)


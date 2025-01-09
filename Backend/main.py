import os
import eel
import subprocess
import threading
from Backend.features import playStartSound

def start():
    eel.init("Frontend")
    threading.Thread(target=playStartSound).start()
    subprocess.Popen(['open', '-a', 'Safari', 'http://localhost:8000/index.html'])
    eel.start('index.html', mode=None, host='localhost', block=True)

if __name__ == '__main__':
    start()
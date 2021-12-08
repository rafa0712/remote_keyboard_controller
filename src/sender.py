from pynput.keyboard import Listener
import pickle
from sender.Socket import Socket

socket = Socket(('192.168.15.2', 6081))

def on_press(key):
    response = {
        'type':'press',
        'key':key
    }
    serialized = pickle.dumps(response)
    socket.send(serialized)

def on_release(key):
    response = {
        'type':'release',
        'key':key
    }
    serialized = pickle.dumps(response)
    socket.send(serialized)

with Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()
    
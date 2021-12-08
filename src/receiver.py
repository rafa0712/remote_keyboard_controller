from receiver.Socket import Socket
from receiver.Handler import Handler
import pickle
from pynput.keyboard import Controller, Key
kb = Controller()
socket = Socket(('', 6081))

while True:
    data = socket.recv(2048)
    data = pickle.loads(data)
    chosen = Handler(data)
    #
    type = data['type']
    key = data['key']
    if (type == 'press'):
        
        kb.press(key)
    else:
        kb.release(key)
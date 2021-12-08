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
    key = data['key']
    chosen = Handler(data)

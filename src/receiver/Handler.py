from pynput.keyboard import Controller
kb = Controller()

options = {
    'press':kb.press,
    'release':kb.release,
}

def Handler(command):
    type = command.get('type')
    return options.get(type)
    


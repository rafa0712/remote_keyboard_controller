import socket

class Socket:
    def __init__(self, target_addr):
        self.target_addr = target_addr
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def send(self, data):
        self.socket.sendto(data, self.target_addr)
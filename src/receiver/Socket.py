import socket

class Socket:
    def __init__(self, bind_addr):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(bind_addr)
    
    def recv(self, size):
        message, addr = self.socket.recvfrom(size)
        return message
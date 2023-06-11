from abc import ABC
import socket
import asyncio
import multiprocessing

class Connection(ABC):

    def __init__(self, port, buffer):
        # Create a datagram socket
        self.server = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = port
        self.buffer = buffer
        # Bind to host and port
        self.server.bind((self.host, self.port))
        print("UDP server up and listening")

    def encode(self, message):
        return message.encode(encoding = 'UTF-8', errors = "strict")
    
    def decode(self, message):
        return message.decode('UTF-8')
class Contacts:

    def __init__(self):
        self.contacts = {
            'eldrich': '192.168.50.10'
        }
        
    def search_contact(self, name):
        if name in self.contacts:
            return self.contacts[name]
        else: 
            return False
        
    def add_contact(self, name, ip_address):
        if self.search_contact(name):
            print("ya existe")
        else:
            self.contacts[name] = ip_address
            print(f'Contact: {name} - Address: {ip_address} Incorporated.')


class Send_Message(Connection):

    async def send_message(self, message, address):
        message_encode = self.encode(message)
        self.server.sendto(message_encode, address)
    
    def run_send(self):
        contacts = Contacts()
        while True:
            name = input("contact: ")
            message = input("mesage: ")
            contact = (contacts.search_contact(name), 5024)
            asyncio.run(self.send_message(message, contact))

if __name__ == "__main__":
    port = 5026
    buffer = 1024
    send = multiprocessing.Process(target=Send_Message(port, buffer).run_send()).start()
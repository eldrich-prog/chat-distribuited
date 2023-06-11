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
            print(f'Contact: \'{name}\' no identified.')
            return False
        
    def add_contact(self, name, ip_address):
        if self.search_contact(name):
            print("ya existe")
        else:
            self.contacts[name] = ip_address
            print(f'Contact: {name} - Address: {ip_address} Incorporated.')


class Send_Message(Connection):
    
    def __validate(self, message) -> bool:
        return True if message != "" else False
    
    def __bug(self, exception) -> None:
        print(f"Something unexpected happened: {exception}")
        self.run_send(5024)

    def choose_contact(self) -> str:
        contacts = Contacts()
        name = input("Contact: ")
        return contacts.search_contact(name)
    
    def write_message(self) -> str:
        message = input("Message: ")
        return message if self.__validate(message) else False
    
    async def send_message(self, message, address) -> int:
        message_encode = self.encode(message)
        self.server.sendto(message_encode, address)

    def run_send(self, port):
        contacts = Contacts()
        while True:
            try:
                contact = self.choose_contact()
                if contact:
                    message = self.write_message()
                if contact and message:
                    asyncio.run(self.send_message(message, (contact, port)))
                    print("Send message.")
            except Exception as ex:
                self.__bug(ex)



if __name__ == "__main__":
    port_socket = 5026
    port_send = 5024
    buffer = 1024
    send = multiprocessing.Process(
        target=Send_Message(port_socket, buffer).run_send(port_send)).start()
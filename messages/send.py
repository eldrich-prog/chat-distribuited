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
        # Encode the message with the given encoding
        return message.encode(encoding = 'UTF-8', errors = "strict")
    
    def decode(self, message):
        # Decode the message with the given encoding
        return message.decode('UTF-8')
    
class Contacts:

    def __init__(self):
        # Port of the server and username of the client
        self.contacts = {
            'eldrich': '192.168.50.10'
        }
        
    def search_contact(self, name):
        # Search for a contact in the contacts dictionary
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


class Write:

    def __validate(self, message):
        return True if message != "" else False

    def write_message(self):
        message = input("Message: ")
        return message if self.__validate(message) else False


class Send_Message(Connection):

    def __init__(self, address, port):
        # Create a datagram socket with the given address and port
        self.address = address
        self.port_address = port
    
    def send_message_group(self):
        # Send a message to all clients
        pass

    def __bug(self, exception) -> None:
        print(f"Something unexpected happened: {exception}")
        self.run_send(5024)


    async def send_message(self, message) -> int:
        # Send the message to the server and return the number of bytes sent
        message_encode = self.encode(message)
        self.server.sendto(message_encode, (self.address, self.port_address))

    def run_send(self):
        # Run the connection with the server and send the messages
        while True:
            try:
                message = self.write_message()
                if message:
                    asyncio.run(self.send_message(message))
                    print("Send message.")
            except Exception as ex:
                self.__bug(ex)



if __name__ == "__main__":
    port_socket = 5026
    port_send = 5024
    buffer = 1024
    send = multiprocessing.Process(
        target=Send_Message(port_socket, buffer).run_send(port_send)).start()
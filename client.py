import socket
import sys


            
class Agenda:

    def __init__(self):
        self.contact = {
            'eldrich':'192.168.50.12',
        }

    def add_contact(self,name = None,address = None):
        if name is None and address is None:
            name = input("Nombre: ").lower()
            address = input("Address: ")
        self.contact.setdefault(name, address)

    def see_contacts(self):
        for cont in self.contact:
            print(cont)

class Chat:

    def __init__(self, HOST, PORT = None):

        if PORT is None: PORT = 5024
        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.sock:
            # Connect to server and send data
            self.sock.connect((HOST, PORT))
            self.write()
            

    def write(self ):
        message = input("Message: ")
        if message == 'exit':
            self.sock.close()
            print('desconectado')
        else:
            self.send(message)
            self.write()

    
    def send(self, message):
        self.sock.sendall(bytes(message + "\n", "utf-8"))
        received = self.reciv()
        print("Sent: {}".format(message))



    def reciv(self):
        received = str(
        self.sock.recv(1024), "utf-8")
        print("Received: {}".format(received))
    
    


if __name__ == '__main__':
    message = Chat("192.168.50.10")


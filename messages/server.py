from abc import ABC
import socket
import asyncio
import multiprocessing

class Connection(ABC):

    def __init__(self):
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = 5024
        self.buffer = 1024

        # Create a datagram socket
        self.server = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
        # Bind to host and port
        self.server.bind((self.host, self.port))
        print("UDP server up and listening")

    def encode(self, message):
        return message.encode(encoding = 'UTF-8', errors = "strict")
    
    def decode(self, message):
        return message.decode('UTF-8')

class Reciv_Message(Connection):

    async def reciv_message(self):
        data_encode, address = self.server.recvfrom(self.buffer)
        data = self.decode(data_encode)
        return data, address
    
    def run_recv(self):
        while (True):
            print("...")
            data, address = asyncio.run(self.reciv_message())
            print(f"message: {data=} send to for {address=}")

if __name__ ==  "__main__":
    recv = multiprocessing.Process(target=Reciv_Message().run_recv()).start()
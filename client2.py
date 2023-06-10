import socket
import logging
import threading
import asyncio

class Client:
    
    def __init__(self, address, port ):
        self.server_address = (address, port)
        self.bufferSize = 1024

        # Create a UDP socket at client side
        self.client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def __encode(self, message):
        return message.encode(encoding = 'UTF-8', errors = 'strict')
    
    def __decode(self, message):
        return message.decode('UTF-8')
    
    async def send_data(self):
            stop = True
            while stop:
                message = str(input("message: "))
                encode = self.__encode(message)
                count = self.client_socket.sendto(encode, self.server_address)
                if message == "False": stop = False
        
    async def recived(self):
            while True:
                data_encode, address = self.client_socket.recvfrom(self.bufferSize)
                data = self.__decode(data_encode)
                print(f"{data=} enviado por {address=}")


if __name__ == "__main__":
    while True:
        client = Client("192.168.50.10", 5024)
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
        logging.info("Main    : before creating thread")
        asyncio.run(client.send_data())
        asyncio.run(client.recived())
        """
        x = threading.Thread(target=client.send_data())
        y = threading.Thread(target=client.recived())
        x.start()
        y.start()
        """ 

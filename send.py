from abc import ABC
import socket
import asyncio
import multiprocessing
import server

class Send_Message(server.Connection):

    async def send_message(self, message, address):
        message_encode = self.encode(message)
        self.server.sendto(message_encode, address)
    
    def run_send(self):
        while True:
            message = input("mesage: ")
            address = ("192.168.50.10", 6001)
            asyncio.run(self.send_message(message, address))

if __name__ == "__main__":
    send = multiprocessing.Process(target=Send_Message().run_send()).start()
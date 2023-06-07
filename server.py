import socketserver
import socket
import threading

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        handle = True
        while handle:
            try:
                print("waiting to receive...")
                data = self.request.recv(1024).strip()
                print("request receive")
                if data == b'exit':
                    exit()

                print("{}  address client".format(self.client_address[0]))
                self.send(data)
            except Exception as ex:
                print(f"Error: {ex}")
    
    def send(self, data):
        self.request.sendall(data.upper())
        
    def close(self):
        MyServer.close()


class Main:

    def __init__(self):
        HOST = socket.gethostbyname(socket.gethostname())
        
        PORT = 5024
        with socketserver.TCPServer((HOST,PORT), MyServer) as server:
            print("run server...")
            server.serve_forever()\
           

if __name__ == '__main__':
    Main()
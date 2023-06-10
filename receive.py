import server
import asyncio
import multiprocessing


class Reciv_Message(server.Connection):

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
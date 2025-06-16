import asyncio, json, os
from colored import fg, attr
from pycolor import print_color
from websockets.server import serve

class ChatServer:
    def __init__(self):
        self.clients: list = []
    async def ClientHandler(self, websocket, path):
        self.clients.append(websocket)
        print(f"{attr(1)}{fg(2)}[+]{attr(0)} Client Connected [{path[1:]}] [{websocket.remote_address[0]}:{websocket.remote_address[1]}]")
        try:
            async for message in websocket:
                if message == '//quit//':
                    print(f"{attr(1)}{fg(1)}[-]{attr(0)} Client Disconnected [{path[1:]}] [{websocket.remote_address[0]}:{websocket.remote_address[1]}]")
                    self.clients.remove(websocket)
                    break
                print(f"{attr(1)}{fg(6)}[=]{attr(0)} {path[1:]} sends {json.loads(message)['message']}")
                for client in self.clients:
                    await client.send(json.dumps({"user": path[1:], "message": json.loads(message)['message']}))
        except:
            print(f"{attr(1)}{fg(1)}[-]{attr(0)} Client Disconnected [{path[1:]}] [{websocket.remote_address[0]}:{websocket.remote_address[1]}]")
            self.clients.remove(websocket)
    async def Server(self):
        async with serve(self.ClientHandler, "localhost", 4500):
            await asyncio.Future()

if __name__ == '__main__':
    os.system('cls')
    print_color("""

 █████╗ ███████╗███████╗    ███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗███████╗██████╗ 
██╔══██╗██╔════╝██╔════╝    ██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
███████║█████╗  ███████╗    █████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   █████╗  ██║  ██║
██╔══██║██╔══╝  ╚════██║    ██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██╔══╝  ██║  ██║
██║  ██║███████╗███████║    ███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║   ███████╗██████╔╝
╚═╝  ╚═╝╚══════╝╚══════╝    ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚══════╝╚═════╝ 

         ██████╗██╗  ██╗ █████╗ ████████╗    ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗ 
        ██╔════╝██║  ██║██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
        ██║     ███████║███████║   ██║       ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝
        ██║     ██╔══██║██╔══██║   ██║       ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗
        ╚██████╗██║  ██║██║  ██║   ██║       ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║
        ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝
    """, fg_color='cyan')
    print_color("\t\t\t\t\t\tCreated by", fg_color='rainbow')
    print_color("\t\t\t\t\tYuvaraja.M CSE-B 1st Year", fg_color='rainbow')
    print("\n")
    asyncio.run(ChatServer().Server())
from colored import fg, attr
from Crypto.Cipher import AES
from pycolor import print_color
import threading, json, sys, base64, os
from websockets.sync.client import connect

class Encryption:
    def __init__(self):
        self.key = b'\xecT%\xd1\xf0vZ\x84\xf2:\n*]r\xd7\x8e'
        self.cipher = AES.new(self.key, AES.MODE_ECB)
    def encrypt(self, data):
        data += ' ' * (AES.block_size - len(data) % AES.block_size)
        encrypted_data = base64.b64encode(self.cipher.encrypt(data.encode())).decode()
        return encrypted_data
    def decrypt(self, data):
        decrypted_data = self.cipher.decrypt(base64.b64decode(data.encode()))
        return decrypted_data.decode()

class ChatClient:
    def __init__(self):
        self.user = input(f'{attr(1)}{fg(3)}Enter the User:{attr(0)} ')
        print(end='\n')
        self.Connect()
    def Connect(self):
        with connect(f"ws://localhost:4500/{self.user}") as server:
            print(f"{attr(1)}{attr(5)}{fg(6)}=> {fg(2)}✅ Connected to the Server as {attr(0)}{attr(1)}{fg(6)}( {self.user} ){attr(0)}")
            print(end='\n')
            threading.Thread(target=self.RecieveDatas, args=(server,)).start()
            while True:
                try:
                    server.send(json.dumps({'message': Encryption().encrypt(input(""))}))
                    sys.stdout.write('\x1b[1A\x1b[2K')
                except KeyboardInterrupt:
                    server.send("//quit//")
                    break
    def RecieveDatas(self, server):
        while True:
            try:
                message_data = json.loads(server.recv())
                print(f"{attr(1)}{fg(160) if self.user == message_data['user'] else fg(6)}{message_data['user']}:{attr(0)} {Encryption().decrypt(message_data['message'])}")
            except:
                break

if __name__ == '__main__':
    os.system('cls')
    print_color("\t\tAES Encrypted Chat Program", fg_color='rainbow')
    print_color("\t\t\tCreated by", fg_color='rainbow')
    print_color("\t\tYuvaraja.M CSE-B 1st Year", fg_color='rainbow')
    print(end='\n')
    ChatClient()
class Local_Server:
    def __init__(self) -> None:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
        self.HOST =  s.getsockname()[0]
        self.PORT = 1997
        self.set_host()
    def set_host(self):
        import json
        data = {"HOST":self.HOST,"PORT":self.PORT}
        with open('src/host.json','r+') as jfile :
            json.dump(data, jfile)
        jfile.close()
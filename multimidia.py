import json
class Local_Server:
    def __init__(self) -> None:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
        self.HOST =  s.getsockname()[0]
        self.PORT = 1997
        self.set_host()
    def set_host(self):
        data = {"HOST":self.HOST,"PORT":self.PORT}
        with open('src/host.json','r+') as jfile :
            json.dump(data, jfile)
        jfile.close()


class FolderNFileHandler:
    def __init__(self,path) -> None:
        self.path = path
    def setFolderPath(self):
        data = {"folder":self.path}
        with open('src/folderpath.json','r+') as jfile :
            json.dump(data, jfile)
        jfile.close()


    def getFolderPath(self):
        with open('src/folderpath.json','r+') as jfile :
            data = json.load(jfile)
            jfile.close()
            return data['folder']


    def get_all_files(self):
        import os
        files = os.listdir(self.path)
        files = [f for f in files if os.path.isfile(self.path+'/'+f)] #Filtering only the files.
        return files


import json
import sys
import os

try:
    import socket
except:
    sys.stdout.write('Something went wrong with Connection')
    sys.stdout.flush()

class RootFolder:
    def __init__(self):
        self.STATIC_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    def getRootFolder(self):
        return self.STATIC_ROOT


class Local_Server:
    def __init__(self) -> None:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
            self.HOST =  s.getsockname()[0]
            self.PORT = 1997
            self.isLocal =False
            self.set_host()
        except:
            self.HOST = '127.0.0.1'
            self.PORT = 1997
            self.isLocal=True
            self.set_host()

    def set_host(self):
        data = {"HOST":self.HOST,"PORT":self.PORT,"isLocal":self.isLocal}
        try:
            with open(r'/src/host.json','r+') as jfile :
                jfile.truncate()
                json.dump(data, jfile)
            jfile.close()
        except:
            pass



class DownloadHandler:

    def get_downloadable_all_files(self,paths):
        try:
            import os
            files = os.listdir(paths)
            files = [f for f in files if os.path.isfile(self.path+'/'+f)] #Filtering only the files.
            return files
        except:
            return []




class FlushAll():
    def ClearMetaData(self):
        try:
            with open(r'UPLOAD.txt','w') as FILE:
                FILE.truncate()
                FILE.close()

        except:
            pass

        try:
            with open(r'DOWNLOAD.txt','w') as FILE:
                FILE.truncate()
                FILE.close()

        except:
            pass

        try:
            with open(r'CONNECTION.txt','w') as FILE:
                FILE.truncate()
                FILE.close()

        except:
            pass


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



class UploadHandler:
    def __init__(self,path="") -> None:
        self.ROOT = RootFolder().getRootFolder()
        if(path!=''):
            self.path=path+"/LFS"
        else:
            self.path = self.get_sys_download_dir_path()+"/LFS"
        self.set_upload_folder_path()

    def set_upload_folder_path(self):
        if(self.path !=''):
            try:
                os.chdir(self.ROOT)
                data = {"UploadFolder":self.path}
                with open(r'src\Uploadfolderpath.json','r+') as jfile :
                    jfile.truncate()
                    json.dump(data, jfile)
                jfile.close()
            except:
                os.chdir(self.ROOT)
                os.system(r"type nul > src\Uploadfolderpath.json")
            finally:
                os.chdir(self.ROOT)
                data = {"UploadFolder":self.path}
                with open(r'src\Uploadfolderpath.json','r+') as jfile :
                    jfile.truncate()
                    json.dump(data, jfile)
                jfile.close()
                  

    def LFSupload_path(self):
        path = self.getFolderPathFromJSON()
        try:
            os.chdir(path)
        except:
            os.mkdir(path)
        finally:
            os.chdir(path) 




    def get_sys_download_dir_path(self):
        """Returns the default downloads path for linux or windows"""
        if os.name == 'nt':
            import winreg
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                location = winreg.QueryValueEx(key, downloads_guid)[0]
            return location
        else:
            return os.path.join(os.path.expanduser('~'), 'downloads')

    def getFolderPathFromJSON(self):
        os.chdir(self.ROOT)
        try:
            with open(r'src\Uploadfolderpath.json','r+') as jfile :
                data = json.load(jfile)
                jfile.close()
                return data['UploadFolder']
        except :
           os.system(r'type nul > src\Uploadfolderpath.json')
        finally:
            with open(r'src\Uploadfolderpath.json','r+') as jfile :
                data = json.load(jfile)
                jfile.close()
                return data['UploadFolder']
            

            



class DownloadHandler:

    def __init__(self,path='') -> None:
        self.ROOT = RootFolder().getRootFolder()
        if path=="":
            self.path=self.get_sys_download_dir_path()
        else:
            self.path = path
        self.setDownloadFolderPath()

    def setDownloadFolderPath(self):
        os.chdir(self.ROOT)
        try:
            data = {"DownloadFolder":self.path}
            with open(r'src\Downloadfolderpath.json','r+') as jfile :
                jfile.truncate()
                json.dump(data, jfile)
            jfile.close()
        except:
            os.system(r'type nul > src\Downloadfolderpath.json')
        finally:
            data = {"DownloadFolder":self.path}
            with open(r'src\Downloadfolderpath.json','r+') as jfile :
                jfile.truncate()
                json.dump(data, jfile)
                jfile.close()

    def getDownloadFolderPath(self):
        os.chdir(self.ROOT)
        with open(r'src\Downloadfolderpath.json','r+') as jfile :
            data = json.load(jfile)
            jfile.close()
            return data['DownloadFolder']


    def get_downloadable_all_files(self):
        try:
            import os
            files = os.listdir(self.path)
            files = [f for f in files if os.path.isfile(self.path+'/'+f)] #Filtering only the files.
            return files
        except:
            return []


    def get_sys_download_dir_path(self):
        """Returns the default downloads path for linux or windows"""
        if os.name == 'nt':
            import winreg
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                location = winreg.QueryValueEx(key, downloads_guid)[0]
            return location
        else:
            return os.path.join(os.path.expanduser('~'), 'downloads')





class FlushAll():
    def __init__(self) -> None:
         self.ROOT = RootFolder().getRootFolder()
    def ClearMetaData(self):
        os.chdir(self.ROOT)
        with open(r'src\folderpath.json','r+') as fp:
            fp.truncate()
            fp.close()
        with open(r'src\host.json','r+') as fp:
            fp.truncate()
            fp.close()
        with open(r'src\folderpath.json','r+') as fp:
            fp.truncate()
            fp.close()
        with open(r'src\Downloadfolderpath.json','r+') as fp:
            fp.truncate()
            fp.close()



class FileChecker():
    def __init__(self):
        self.ROOT = RootFolder().getRootFolder()
        os.chdir(self.ROOT)

    def getUploadFileStatus(self):
        if(os.path.exists(r'src\\Uploadfolderpath.json')):
            try:
                with open(r'src\Uploadfolderpath.json','r+') as jfile :
                    data = json.load(jfile)
                    jfile.close()
                    return data['UploadFolder']
            except:
                return "Upload json error"
        else:
            return False

    def getDownloadFileStatus(self):
       
        if(os.path.exists(r'src\\Downloadfolderpath.json')):
            try:
                with open(r'src\Downloadfolderpath.json','r+') as j2file :
                    data2 = json.load(j2file)
                    j2file.close()
                    return data2['DownloadFolder']
            except:
                return "download json error"
        else:
            return False




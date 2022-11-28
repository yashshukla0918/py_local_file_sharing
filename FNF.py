from multimedia import RootFolder
import os
class FolderPaths:
    def __init__(self):
        self.ROOT = RootFolder().getRootFolder()
        self.UPLOAD_PATH=""
        self.DOWNLOAD_PATH=""
        self.CONN='0'
        try:
            with open(r'UPLOAD.txt','r+') as UP_FILE:
                self.UPLOAD_PATH = UP_FILE.read()
                UP_FILE.close()
            with open(r'DOWNLOAD.txt','r+') as DW_FILE:
                self.DOWNLOAD_PATH = DW_FILE.read()
                DW_FILE.close()
            with open(r'CONNECTION.txt','r+') as Connf:
                self.CONN = Connf.read()
                Connf.close()

        except Exception as e:
            print("Constructor ERROR:"+str(e))
            
            

# 
# Getter
# 

    def getUploadFolderPath(self):
        if str(self.UPLOAD_PATH)!="":
            return self.UPLOAD_PATH
        else:
            self.setUploadFolderPath(self.default_folder_path())
            return self.default_folder_path()




    def getDownloadFolderPath(self):
        if str(self.DOWNLOAD_PATH)!="":
            return self.DOWNLOAD_PATH
        else:
            self.setDownloadFolderPath(self.default_folder_path())
            return self.default_folder_path()



    def getMaxConnection(self):
        if self.CONN!='0':
            return self.CONN
        else:
            self.setMaxConnection('4')
            return '4'


# 
# Setter
# 

    def setUploadFolderPath(self,path):
        try:
            with open(r'UPLOAD.txt','a') as UP_FILE:
                UP_FILE.truncate()
                UP_FILE.write(path)
                UP_FILE.close()
        except:
            pass
            


    def setDownloadFolderPath(self,path):
        try:
            with open(r'DOWNLOAD.txt','a') as FILE:
                FILE.truncate()
                FILE.write(path)
                FILE.close()
        except:
            pass

            


    def setMaxConnection(self,con:str):
        try:
            with open(r'CONNECTION.txt','a') as FILE:
                FILE.truncate()
                FILE.write(con)
                FILE.close()
        except:
            pass


# 
# Default folder path
# 

    def default_folder_path(self):
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


    def get_downloadable_all_files(self):
        dpath = self.getDownloadFolderPath()
        try:
            files = os.listdir(dpath)
            files = [f for f in files if os.path.isfile(dpath+'/'+f)]#Filtering only the files.
            return files
        except:
            return []



try:
    import sqlite3
    import os

except ImportError:
    print("Lib not found")



class DB:
    def __init__(self):
        try:
            sqlite3.connect('LFS.db')
        except:
            self.conn=sqlite3.connect('LFS.db')
        finally:
            self.conn = sqlite3.connect('LFS.db')
        self.__check_table_exists()


    def __check_table_exists(self):
        c = self.conn.cursor()
        c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='LFS_TABLE' ''')
        if (c.fetchone()[0]==1): 
            print('[SUCCESS] : DATABASE CONNECTED SUCCESSFULLY!  ')
        else:
            try:
                c.execute('''CREATE TABLE LFS_TABLE
                (ID CHAR(6) PRIMARY KEY NOT NULL,
                UPLOAD_FOLDER_PATH VARCHAR(500) ,
                DOWNLOAD_FOLDER_PATH VARCHAR(500) ,
                MAX_CONNECTION INT ,
                HOST VARCHAR(12) ,
                PORT INT ,
                isLocal BOOLEAN ,
                isSecure BOOLEAN 
                );''')
                self.__CHECK_TABLE_VALUE()
                self.conn.commit()
            except Exception as e:
                print(str('[ERROR] : Something went wrong with create table :( ').upper())
                print("[ERROR] : "+str(e).upper())





    def __CHECK_TABLE_VALUE(self):
        __c = self.conn.cursor()
        path = self.default_folder_path()
        try:
            __statment = "select port from LFS_TABLE where id='host';"
            res=__c.execute(__statment)
            if(bool(res.fetchone()) == False):
                __c.execute('''INSERT INTO LFS_TABLE (ID,UPLOAD_FOLDER_PATH,DOWNLOAD_FOLDER_PATH,MAX_CONNECTION,HOST,PORT,isLocal,isSecure) VALUES ('host',"'''+str(path)+'''", "'''+str(path)+'''",4,"127.0.0.1",1997,true,false);''')
                self.conn.commit()
        except Exception as e:
            print(str("[ERROR] : "+e).upper())
    
            




    def __RUN_STATEMENT(self,data):
        c = self.conn.cursor()
        __data = c.execute("SELECT "+data+" FROM LFS_TABLE WHERE ID='host';")
        __result = __data.fetchone()
        if(bool(__result)):
            return __result[0]
        else:
            False 





    def __INSERT_AND_UPDATE(self,*args):
            c = self.conn.cursor()
            c.execute(args[0])
            self.conn.commit()
            print(str('[success] : set '+args[1]+' to '+str(args[2])).upper())

        



    def getUploadFolderPath(self):
        result = self.__RUN_STATEMENT('UPLOAD_FOLDER_PATH')
        if(bool(result)):
            return str(result)
        else:
            return self.default_folder_path()
                





    def getDownloadFolderPath(self):
            result = self.__RUN_STATEMENT('DOWNLOAD_FOLDER_PATH')
            if(bool(result) == True):
                return str(result)
            else:
                return self.default_folder_path()





    def getMaxConnection(self):
            result = self.__RUN_STATEMENT("MAX_CONNECTION")
            if(bool(result)== True ):
                return result
            else:
                return 4





    def getHOST(self):
            result = self.__RUN_STATEMENT("HOST")
            if(bool(result) ==True):
                return result
            else:
                pass




    def getPORT(self):
            result = self.__RUN_STATEMENT("PORT")
            if(bool(result)==True):
                return result
            else:
                pass





    def get_isLocal(self):
            result = self.__RUN_STATEMENT("isLocal")
            if(bool(result) == True):
                return result
            else:
                pass





    def get_isSecure(self):
            result = self.__RUN_STATEMENT("isSECURE")
            return bool(result)






    def setUploadFolderPath(self,path=""):
            if(self.getUploadFolderPath() and path!=''):
                __Statement = "UPDATE LFS_TABLE SET UPLOAD_FOLDER_PATH = '"+str(path)+"' WHERE ID='host';"
                self.__INSERT_AND_UPDATE(__Statement,"upload folder",path)






    def setDownloadFolderPath(self,path=""):
            if(self.getDownloadFolderPath() and path!=''):
                __Statement = "UPDATE LFS_TABLE SET DOWNLOAD_FOLDER_PATH = '"+str(path)+"' WHERE ID='host';"
                self.__INSERT_AND_UPDATE(__Statement,"download folder",path)






    def setMaxConnection(self,max=0):
            if(self.getMaxConnection() and max!=0):
                max = int(max)
                __Statement = f"UPDATE LFS_TABLE SET MAX_CONNECTION = '{max}' WHERE ID='host';"
                self.__INSERT_AND_UPDATE(__Statement,"MAX CONNECTION",max)





    def setHost(self):
        import socket
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
            __HOST =  s.getsockname()[0]
            __PORT = 1997
            __isLocal = False
        except:
            __HOST = '127.0.0.1'
            __PORT = 1997
            __isLocal= True

        __Statement = f"UPDATE LFS_TABLE SET HOST = '{__HOST}', PORT =' {__PORT}', isLocal = '{__isLocal}'  WHERE ID='host';"
        self.__INSERT_AND_UPDATE(__Statement,"HOST ",str(__HOST))





    def set_isScure(self,isSecure=''):
            if(self.get_isSecure() and isSecure!=''):
                isSecure = bool(isSecure)
                __Statement = f"UPDATE LFS_TABLE SET isSecure= '{isSecure}' WHERE ID='host';"
                self.__INSERT_AND_UPDATE(__Statement,"Secure Transfer",isSecure)

                


    def default_folder_path(self):
        if os.name == 'nt':
            import winreg
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                location = winreg.QueryValueEx(key, downloads_guid)[0]
            return location
        else:
            return os.path.join(os.path.expanduser('~'), 'downloads')









class StaticData:     
    def get_downloadable_all_files(self):
        dpath = self.getDown()
        try:
            files = os.listdir(dpath)
            files = [f for f in files if os.path.isfile(dpath+'/'+f)]#Filtering only the files.
            return files
        except:
            return []





    def getRootFolder(self):
        dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        return dir 




    def getDown(self):
        d = DB()
        dpath =d.getDownloadFolderPath()
        return str(dpath)

from flask import Flask, render_template, request,redirect
from flask import send_file
from waitress import serve
import os
import sys
import sqlite3


#Configuring Flask app
app = Flask(__name__,)
app.static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates\static")



#Import Static DATA 
#Project folder path(root)
#Download folder path (from where user can download)
#get all files name as list from downloadable folder

from db import StaticData
database = StaticData()




with sqlite3.connect('LFS.db') as conn:
   __cur = conn.cursor()
   try:
       __result = __cur.execute("select * from LFS_TABLE where ID='host' ;")
   except sqlite3.OperationalError :
      os.system("type nul > LFS.db")
      __cur.execute('''CREATE TABLE LFS_TABLE
                (ID CHAR(6) PRIMARY KEY NOT NULL,
                UPLOAD_FOLDER_PATH VARCHAR(500) ,
                DOWNLOAD_FOLDER_PATH VARCHAR(500) ,
                MAX_CONNECTION INT ,
                HOST VARCHAR(12) ,
                PORT INT ,
                isLocal BOOLEAN ,
                isSecure BOOLEAN 
                );''')
      __cur.execute('''CREATE TABLE LFS_CLIENT(IP CHAR(13) PRIMARY KEY NOT NULL,NAME VARCHAR);''')
      __cur.execute('''CREATE TABLE LFS_OTP(OTP INT(6) PRIMARY KEY NOT NULL);''')
      conn.commit()
      try:
         __cur.execute('''INSERT INTO LFS_TABLE (ID,UPLOAD_FOLDER_PATH,DOWNLOAD_FOLDER_PATH,MAX_CONNECTION,HOST,PORT,isLocal,isSecure) VALUES ('host',"/path", "/path",4,"127.0.0.1",1997,true,false);''')
         __cur.execute('''INSERT INTO LFS_TABLE (OTP) VALUES (123456);''')
      except:
         pass
      conn.commit()
   finally:
      __result = __cur.execute("select * from LFS_TABLE where ID='host' ;")
      __result = __result.fetchall()[0]
      __downloadFolder =str( __result[2])
      __uploadFolder = str(__result[1])
      __max_connection = __result[3]
      __host_ip = str(__result[4])
      __host_port = __result[5]
      print(str('[message] : Application is active on : http://'+str(__host_ip)+":"+str(__host_port)).upper())
      print(str('[message] : Application Download Folder : '+__downloadFolder).upper())
      print(str('[message] : Application Upload Folder : '+__uploadFolder).upper())
      print(str('[message] : Application Max Connection : '+str(__max_connection)).upper())



def getClientAuth(client_Ip):
   with sqlite3.connect("LFS.db") as conn:
      __cursor = conn.cursor()
      __result = __cursor.execute("select * from LFS_CLIENT where IP = '"+client_Ip+"';")
      data =__result.fetchone()
      try:
         if(data == None):
            return False
         else:
            return True
      except Exception as e:
         print(e)
         return False

def addClient(ip):
   with sqlite3.connect("LFS.db") as conn:
      __cursor = conn.cursor()
      try:
          __result = __cursor.execute("INSERT INTO LFS_CLIENT (IP,NAME) VALUES ('"+str(ip)+"','NA');")
          conn.commit()
      except Exception as e:
         print(e)


def verifyOTP(otp):
   with sqlite3.connect("LFS.db") as conn:
      __cursor = conn.cursor()
      __result = __cursor.execute("select ID from LFS_OTP where otp = '"+otp+"';")
      data =__result.fetchone()
      try:
         if(data == None):
            return False
         else:
            addClient(request.remote_addr)
            return True
      except Exception as e:
         print(e)
         return False




@app.route('/authenticate',endpoint="auth", methods = ['GET', 'POST'])
def auth():
   if request.method == "POST":
      data = request.form.get('otp')
      if(verifyOTP(data)):
         return redirect("/")
      return render_template('authenticate.html')



@app.route('/')
def home():
   os.chdir(database.getRootFolder())
   if(getClientAuth(str(request.remote_addr))):
      return render_template('index.html')
   else:
      return render_template('authenticate.html')


@app.route('/getupPath')
def getupPath():
   if(getClientAuth(request.remote_addr)):
      return str(__uploadFolder)
   return redirect('/')

@app.route('/getConnection')
def getConnection():
   if(str(request.remote_addr)== __host_ip):
      return render_template('connected_device.html')
   return redirect('/')


@app.errorhandler(404)
def not_found(e):
   return render_template('error.html')



@app.errorhandler(500)
def internal_error(error):
   return 'Something went wrong 500 '



@app.route('/Upload',endpoint="upload")
def upload():
   if(str(request.remote_addr)):
      return render_template('upload.html')
   return redirect('/')    



@app.route('/Download',endpoint="download")
def download():
   if(str(request.remote_addr)):
      return render_template('download.html')
   return redirect('/')



@app.route('/uploader',endpoint="upload_file", methods = ['GET', 'POST'])
def upload_file():
   if(str(request.remote_addr)):
      os.chdir(__uploadFolder)
      if(os.path.exists(__uploadFolder+"/LFS") == False):
         os.mkdir("LFS")
      os.chdir(__uploadFolder+"/LFS")
      if(os.path.exists(__uploadFolder+"/LFS/"+str(request.remote_addr)) == False):
         os.mkdir(str(request.remote_addr))
      os.chdir(__uploadFolder+"/LFS/"+request.remote_addr)
      if request.method == 'POST':
         files = request.files.getlist('filemultiple') 
         if(files):
            for file in files:
               file.save(file.filename)
            return render_template('success.html')
         else:
            return render_template('failed.html')
   return redirect('/')


@app.route('/Files')
def Files():
   if(str(request.remote_addr)):
      file_list = database.get_downloadable_all_files() #folder_details.get_downloadable_all_files()
      return file_list
   return redirect('/')


@app.route('/getFiles/<file_name>')
def getFile(file_name):
   if(str(request.remote_addr)):
      return send_file(__downloadFolder+"\\"+file_name) 
   return redirect('/')


@app.route('/getCon', endpoint="getConnectionList")
def getConnectionList():
   if(str(request.remote_addr) == __host_ip):
      with sqlite3.connect("LFS.db") as conn:
         __cur = conn.cursor()
         __result = __cur.execute("select * from LFS_CLIENT;")
         __result = __result.fetchall()
         if(__result != None):
            return __result
   return redirect('/')


@app.route('/remove/<ip>')
def removeUser(ip):
   if(str(request.remote_addr)):
      with sqlite3.connect("LFS.db") as conn:
         try:
            __cur = conn.cursor()
            result =__cur.execute("delete from LFS_CLIENT where IP = '"+str(ip)+"' ;")
            conn.commit()
            return '1'
         except:
            return '0'
      return '0'
   return redirect('/')


@app.route('/saveName/<ip>/<name>')
def saveName(ip,name):
   if(str(request.remote_addr)):
      with sqlite3.connect("LFS.db") as conn:
         try:
            __cur = conn.cursor()
            result =__cur.execute("update LFS_CLIENT set NAME='"+name+"' where IP = '"+str(ip)+"' ;")
            conn.commit()
            return '1'
         except:
            return '0'
      return '0'  
   return redirect('/')


mode="prod"
#mode="dev"

 
def runServer():
   import os

   HOST = __host_ip
   PORT = __host_port

   x=os.path.join(os.path.dirname(os.path.abspath(__file__)))
   os.chdir(x)


   if(mode=="dev"):
      app.run(host=HOST,port=PORT,debug=True)
   else:
      sys.stdout.write("Local File Sharing [ LFS ] server started\n")
      sys.stdout.flush()
      try:
         thread = int(__max_connection)
      except:
         sys.stdout.write("Invalid Max connection value given [EXPECTED an Integer]\n")
         sys.stdout.flush()
      serve(app,host=HOST,port=PORT,threads=thread)



if __name__ =="__main__":
   runServer()
 
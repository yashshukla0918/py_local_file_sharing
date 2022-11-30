from flask import Flask, render_template, request
from flask import send_file
from waitress import serve
import os
import sys
import sqlite3



app = Flask(__name__,)
app.static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates\static")


from db import StaticData
database = StaticData()



with sqlite3.connect('LFS.db') as conn:
   __cur = conn.cursor()
   __result = __cur.execute("select * from LFS_TABLE where ID='host' ;")
   __result = __result.fetchall()[0]
   __downloadFolder =str( __result[2])
   __uploadFolder = str(__result[1])
   __max_connection = __result[3]
   __host_ip = str(__result[4])
   __host_port = __result[5]
   __isLocal = __result[6]
   __isSecure = __result[7]
   print(str('[message] : Application is Local Host : '+str(__isLocal)).upper())
   print(str('[message] : Application Download Folder : '+__downloadFolder).upper())
   print(str('[message] : Application Upload Folder : '+__uploadFolder).upper())
   print(str('[message] : Application is Sercure : '+str(bool(__isSecure))).upper())
   print(str('[message] : Application Max Connection : '+str(__max_connection)).upper())





@app.route('/')
def home():
      return render_template('index.html', IF = __isLocal) 
   
@app.route('/getupPath')
def getupPath():
  #folder_details.getUploadFolderPath()
   return str(__uploadFolder)

@app.errorhandler(404)
def not_found(e):
   return render_template('error.html')

@app.errorhandler(500)
def internal_error(error):
    return render_template('Something went wrong 500 '), 500

@app.route('/Upload',endpoint="upload")
def upload():
   if(__isLocal == False):
      return render_template('static_upload.html')
   else:
      return render_template('upload.html')

      
@app.route('/Download',endpoint="download")
def download():
   if(__isLocal == False):
       return render_template("static_download.html")
   else:
      return render_template('download.html')


@app.route('/uploader',endpoint="upload_file", methods = ['GET', 'POST'])
def upload_file():
   os.chdir(__uploadFolder)
   if request.method == 'POST':
      files = request.files.getlist('filemultiple') 
      if(files):
         for file in files:
            file.save(file.filename)
         return render_template('success.html')
      else:
         return render_template('failed.html')

@app.route('/Files')
def Files():
   file_list = database.get_downloadable_all_files() #folder_details.get_downloadable_all_files()
   return file_list


@app.route('/getFiles/<file_name>')
def getFile(file_name):
   return send_file(__downloadFolder+"\\"+file_name) 




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
         thread = __max_connection
      except:
         sys.stdout.write("Invalid Max connection value given [EXPECTED an Integer]\n")
         sys.stdout.flush()
         thread=6
      serve(app,host=HOST,port=PORT,threads=thread)



if __name__ =="__main__":
   runServer()
 
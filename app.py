from flask import Flask, render_template, request
from flask import send_file
from waitress import serve
import os
import sys


def emit_error():
   sys.stdout.write(os.getcwd()+"\n")
   sys.stdout.flush()

app = Flask(__name__,)
app.static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates\static")

from multimedia import Local_Server,DownloadHandler
from FNF import FolderPaths
# from multimedia import Local_Server,DownloadHandler,UploadHandler,FileChecker
# if(FileChecker().getUploadFileStatus()):
#    print("UPLOAD STATUS"+FileChecker().getUploadFileStatus())
#    print("DOWNLOAD STATUS"+FileChecker().getDownloadFileStatus())
#    upload_hndlr =UploadHandler()
# else:
#    upload_hndlr =UploadHandler()

# if(FileChecker().getDownloadFileStatus()):
#    print("DOWNLOAD STATUS"+FileChecker().getDownloadFileStatus())
#    download_hndlr = DownloadHandler(FileChecker().getDownloadFileStatus())
# else:
#    download_hndlr = DownloadHandler()
server_detail = Local_Server()
folder_details = FolderPaths()
downloader = DownloadHandler()

@app.route('/')
def home():
   
   if(server_detail.isLocal):
      return render_template('static_index.html') 
   else:  
      return render_template('index.html') 


@app.errorhandler(404)
def not_found(e):
   return render_template('error.html')


@app.route('/Upload',endpoint="upload")
def upload():
   return render_template('upload.html')

   
   
@app.route('/Download',endpoint="download")
def download():
   return render_template('download.html')

   
   

@app.route('/uploader',endpoint="upload_file", methods = ['GET', 'POST'])
def upload_file():
   os.chdir(folder_details.getUploadFolderPath())
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
   file_list = folder_details.get_downloadable_all_files()
   return file_list


@app.route('/getFiles/<file_name>')
def getFile(file_name):
   return send_file(folder_details.getDownloadFolderPath()+"\\"+file_name) 

# from os import system
mode="prod"#"dev"
# mode="dev"
def runServer():
   import os
   x=os.path.join(os.path.dirname(os.path.abspath(__file__)))
   os.chdir(x)
   server_detail = Local_Server()
   if(mode=="dev"):
      app.run(host=server_detail.HOST,port=server_detail.PORT,debug=True)
   else:
      sys.stdout.write("Local File Sharing [ LFS ] server started\n")
      sys.stdout.flush()
      serve(app,host=server_detail.HOST,port=server_detail.PORT,threads=int(folder_details.getMaxConnection()))

     
runServer() 
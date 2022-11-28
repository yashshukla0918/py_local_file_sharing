from flask import Flask, render_template, request
from flask import send_file
from waitress import serve
import os
import sys


app = Flask(__name__,)
app.static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates\static")

from multimedia import Local_Server

from FNF import FolderPaths


server_detail = Local_Server()

folder_details = FolderPaths()




@app.route('/')
def home():
   if(server_detail.isLocal ):
      return render_template('static_index.html') 
   else:  
      return render_template('index.html') 




@app.route('/getupPath')
def getupPath():
   f=folder_details.getUploadFolderPath()
   return str(f)



@app.errorhandler(404)
def not_found(e):
   return render_template('error.html')



@app.route('/Upload',endpoint="upload")
def upload():
   if(server_detail.isLocal ):
      return render_template('static_upload.html')
   else:
      return render_template('upload.html')

   

   
@app.route('/Download',endpoint="download")
def download():
   if(server_detail.isLocal ):
       return render_template("static_download.html")
   else:
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





mode="prod"
mode="dev"
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
      try:
         thread = int(folder_details.getMaxConnection())
      except:
         sys.stdout.write("Invalid Max connection value given [EXPECTED an Integer]\n")
         sys.stdout.flush()
         thread=6
      serve(app,host=server_detail.HOST,port=server_detail.PORT,threads=thread)


runServer() 
from flask import Flask, render_template, request
from flask import send_file
from multimidia import Local_Server
from multimidia import FolderNFileHandler
import os
import json

static_path="D:\PHOTOS\GO karting"
fnf = FolderNFileHandler(static_path)
fnf.setFolderPath()
app = Flask(__name__,)
app.static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates\static")

@app.route('/')
def home():   
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
   import Download_path
   Download_path.set_path()
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
   file_list = fnf.get_all_files()
   return file_list


@app.route('/getFiles/<file_name>')
def getFile(file_name):
      return send_file(fnf.getFolderPath()+"\\"+file_name) 

# from os import system
server_detail = Local_Server()
app.run(server_detail.HOST,server_detail.PORT,debug=True)

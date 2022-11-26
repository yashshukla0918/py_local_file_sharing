from flask import Flask, render_template, request
from Ip_fetcher import Local_Server
import os
import json



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
     


# from os import system
server_detail = Local_Server()
app.run(server_detail.HOST,server_detail.PORT,debug=True)

from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)


@app.route('/')
def render_file():
   return render_template('upload.html')


@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':

      
      try:
         f = request.files['file']

         f.save("uploads/"+f.filename)
         print(f.filename)

         
         return "<script>location.href = \"/\";</script>"
      except:

         
         return "<script>location.href = \"/\";</script>"


@app.route('/dir')
def dir():
   
   path = "uploads"
   file_list = os.listdir(path)
   value_list = file_list
      
   return render_template('dir.html', values=value_list)




@app.route('/del/<path:filename>')
def my_form_post(filename):
   print(filename)

   os.remove('uploads/'+filename)

   return "<script>location.href = \"/dir\";</script>"
    

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
   return send_from_directory(directory='uploads', filename=filename)




      
if __name__ == '__main__':
   #서버 실행
   #app.run(debug = True)
   app.run(host='0.0.0.0',port='81', threaded=True)

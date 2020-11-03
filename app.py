#------flask libraries code---------------------------------
from flask import Flask
import requests

import your_ml_file_name *

app = Flask(__name__)
#----routing img path code----------------------------------
@app.route('/faceRecog/<path:url>')
def faceRecog(url):
    imgfile = requests.get(url, allow_redirects=True)
    response = Your_ml_fuction(imgfile.content)
    return response
    
def Your_ml_fuction(img):
    
    return "working" #return score
    
#--------------app call initial-----------------------------
if __name__=='__main__':
    app.run()

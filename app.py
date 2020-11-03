#------flask libraries code---------------------------------
from flask import Flask
import requests
# import cv2
# import numpy as np
# import face_recognition
# import os


app = Flask(__name__)

# for cls in myList:
    # curImg = cv2.imread(path + '/' + cls)
    # images.append(curImg)
    # classNames.append(os.path.splitext(cls)[0])
# print(images)

# def findEncodings(images):
    # encodeList=[]
    # for img in images:
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # encode = face_recognition.face_encodings(img)[0]
        # encodeList.append(encode)
    # return encodeList

# encodeListKnown = findEncodings(images)

#----routing img path code----------------------------------
@app.route('/faceRecog/<path:url>')
def faceRecog(url):
    url = url.replace("/alt", "?alt") #url not getting ?
    url = requests.utils.unquote(url)  #converting special characters to utf - 8
    url =url[:-1]  # removing last ' / '
    print(url)
    r = requests.get(url, allow_redirects=True)
    with open('test.jpg', 'wb') as f:
        f.write(r.content)
    response = 'working'   #(url.split('.jpg')[0]).split('/')[-1] #myMLFunction()
    return response
 
#----routing img path code----------------------------------
@app.route('/StoreImg/<path:url>')
def faceRecog(url):
    url = url.replace("/alt", "?alt") #url not getting ?
    name = (url.split('.jpg')[0]).split('/')[-1]
    url = requests.utils.unquote(url)  #converting special characters to utf - 8
    url =url[:-1]  # removing last ' / '
    print(url)
    r = requests.get(url, allow_redirects=True)
    with open('data/'+name+'.jpg', 'wb') as f:
        f.write(r.content)
    response = 'Image added'
    return response
# def myMLFunction():
    # imgg = cv2.imread("test.jpg")
    # imgS = cv2.resize(imgg,(0,0),None,0.25,0.25)
    # imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    # facesCurFrame = face_recognition.face_locations(imgS)
    
    # encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    # for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        # matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        # faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        # matchIndex = np.argmin(faceDis)
        
        # if matches[matchIndex]:
            # name=classNames[matchIndex].upper()
    # return name
#--------------app call initial-----------------------------
if __name__=='__main__':
    app.run(debug=True)
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pyrebase

config={
	"apiKey": "AIzaSyDlOx0qe0T9pp-NiDUrzBZikNTY6NlCIu8", #webkey
	"authDomain": "ml-language.firebaseapp.com", #프로젝트ID
	"databaseURL": "https://ml-language.firebaseio.com/", #database url
	"storageBucket": "ml-language.appspot.com/" #storage
}

cred = credentials.Certificate("C:\capstone\ml-language-firebase-adminsdk-w9pqi-88584bf504.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://ml-language.firebaseio.com/"})

ref = db.reference('ml-language/google_sentiment') # DB레버런스 선언
#ref.update({"name" : "VR 서비스"}) #DB값 변경(업데이트)
print(ref.get())
firebase = db.database()
files = db.child("files").get().val() #딕셔너리로 반환된다.
print(files)
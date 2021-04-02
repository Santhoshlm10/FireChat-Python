#import the firebase module
from firebase import firebase  

#copy and paste your firebase.io URL HERE
firebase = firebase.FirebaseApplication('<YOUR FIREBASE URL>', None)  

#FireChat will be the child goup of the main URL
result = firebase.get('/FireChat/', '')  
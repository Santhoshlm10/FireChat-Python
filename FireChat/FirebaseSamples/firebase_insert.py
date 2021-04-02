#import firebase and datetime module first
from firebase import firebase
import datetime

firebase = firebase.FirebaseApplication('<YOUR FIREBASE URL>', None)
data = {'name': 'Firechat Bot',
        'message': 'Hey!, Weclome to firechat',
        'time': datetime.datetime.now()
        }
result = firebase.post('/FireChat/', data)
print(result)

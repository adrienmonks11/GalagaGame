import firebase_admin as fb
from firebase_admin import credentials, initialize_app, firestore
#from google.cloud import firestore

def connect():
    # Get path to credentials file
    json_path = "keys/team6-Key.json"

    #we don't want to initialize the app multiple times so this will check if it is not running
    if not fb._apps:
        #if not running, get the credentials from the json path, and initialize the app
        cred = fb.credentials.Certificate(json_path)
        fb.initialize_app(cred) #initializing app

    db = firestore.client()
    
    high_scores = db.collection('High_Scores')
    
    # Return the high scores to the game
    return high_scores 


def create_score(score, player, firestore):
    return firestore.collection("scores").doc().create("user: " + player,
                                                    "score: " + score)

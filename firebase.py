import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def authenticate():
    cred = credentials.Certificate(
        'keys/team6-Key.json')

    app = firebase_admin.initialize_app(cred)

    db = firestore.client()
    return db

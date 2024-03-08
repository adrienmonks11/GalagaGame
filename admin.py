import firebase_admin
from firebase_admin import firestore
import json
import sys
import uuid
import firebase
import os
import subprocess

from firebase import authenticate

db = authenticate()


class HighScore:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def to_dict(self):
        entry = {"name": self.name, "score": self.score}
        return entry

    def from_dict(source):
        entry = HighScore(source["name"], source["score"])
        return entry

# Retrieve top 5 scores from Firebase


def get_top_scores():
    scores_ref = db.collection("HighScores")
    TopFiveScores = scores_ref.order_by(
        "score", direction=firestore.Query.DESCENDING).limit(5)
    results = TopFiveScores.stream()
    TopScores = []
    for doc in results:
        TopScores.append(doc.get("score"))
    return TopScores

# Add score to Firebase


def put_score(score, name):
    scores_ref = db.collection("HighScores")
    scores_ref.document(name).set(HighScore(name, score).to_dict())

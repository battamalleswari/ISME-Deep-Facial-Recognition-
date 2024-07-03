import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionrealtime-f6b2a-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "41002":
        {
            "name": "Parimal Adini",
            "major": "Technical Lead",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "4092":
        {
            "name": "Neeraja Bhogadhi",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "41155":
        {
            "name": "Triveni Tppr",
            "major": "Physics",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

        "4077":
        {
            "name": "Sampath Batchu",
            "major": "MicroBiology",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

        "41328":
        {
            "name": "Asish Gupta",
            "major": "MicroBiology",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

        "42285":
        {
            "name": "JAGADEESH",
            "major": "MATHS",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

        "4034":
        {
            "name": "A PAVAN VIVEK",
            "major": "SCIENTIST",
            "starting_year": 2022,
            "total_attendance": 8,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

        
}

for key, value in data.items():
    ref.child(key).set(value)
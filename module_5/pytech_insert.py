print("Denae Luna")
print("CSD 310")
print("20 June 2021")

import json
# establish connection
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.xbgps.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech['students']

#data to exported
fj1007 = {
    "first_name": "Fred",
    "last_name" : "Johnson",
    "student_id": "1007"
}

sb1008 = {
    "first_name": "Sandra",
    "last_name" : "Bullock",
    "student_id" : "1008"
}

dr1009 = {
    "first_name" : "Daniel",
    "last_name" : "Ratcliffe",
    "student_id" : "1009"
}

#creates documents in students
fred_student_id = db.insert_one(fj1007).inserted_id
sandra_student_id = db.insert_one(sb1008).inserted_id
daniel_student_id = db.insert_one(dr1009).inserted_id

#concenates string for names of students
fj = str(fj1007.get("first_name", "none") + " " + fj1007.get("last_name","none"))
sb = str(sb1008.get("first_name", "none") + " " + sb1008.get("last_name","none"))
dr = str(dr1009.get("first_name", "none") + " " + dr1009.get("last_name","none"))

#prints document 
print("\n-- INSERTED DOCUMENTS --")
print(f"Inserted student record {fj} into the students collection with document {fred_student_id}")
print(f"Inserted student record {sb} into the students collection with document {sandra_student_id}")
print(f"Inserted student record {dr} into the students collection with document {daniel_student_id}")

print("\n\n\tEnd of Program, press any key to exit...")
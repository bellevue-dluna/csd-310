print("Denae Luna")
print("CSD 310")
print("20 June 2021")

import json
# establish connection
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.xbgps.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

# creates docs collection 
docs = db.students.find({})

print("\n\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    sid = doc.get("student_id")
    fn = doc.get("first_name")
    ln = doc.get("last_name")
    print(f"Student ID: {sid}")
    print(f"First Name: {fn}")
    print(f"Last Name: {ln}\n")

print("\n\n-- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY --")
doc = db.students.find_one({"student_id": "1007"})
sid = doc.get("student_id")
fn = doc.get("first_name")
ln = doc.get("last_name")
print(f"Student ID: {sid}")
print(f"First Name: {fn}")
print(f"Last Name: {ln}")

print("\n\n\tEnd of Program, press any key to exit...")
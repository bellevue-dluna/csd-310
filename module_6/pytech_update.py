print("Denae Luna")
print("CSD 310")
print("24 June 2021")

import json
# establish connection
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.xbgps.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

# creates docs collection 
docs = db.students.find({})

new = db.students.find_one_and_update({"student_id": "1007"}, {"$set": {"last_name": "Johnson"}})


print("\n\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    sid = doc.get("student_id")
    fn = doc.get("first_name")
    ln = doc.get("last_name")
    print(f"Student ID: {sid}")
    print(f"First Name: {fn}")
    print(f"Last Name: {ln}\n")

doc = db.students.find_one_and_update({"student_id": "1007"}, {"$set": {"last_name": "Smith"}})
old = doc.get("last_name")
doc = db.students.find_one({"student_id": "1007"})
new = doc.get("last_name")

print(f"Student with ID of 1007 last name updated from {old} to {new}.")

print("\n\n-- DISPLAYING STUDENTS DOCUMENT 1007 --")
doc = db.students.find_one({"student_id": "1007"})
sid = doc.get("student_id")
fn = doc.get("first_name")
ln = doc.get("last_name")
print(f"Student ID: {sid}")
print(f"First Name: {fn}")
print(f"Last Name: {ln}")

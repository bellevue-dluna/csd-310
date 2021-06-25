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

print("\n\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    sid = doc.get("student_id")
    fn = doc.get("first_name")
    ln = doc.get("last_name")
    print(f"Student ID: {sid}")
    print(f"First Name: {fn}")
    print(f"Last Name: {ln}\n")

print("\n\n-- INSERT STATEMENT --")
kh1010 = {
    "first_name" : "Kevin",
    "last_name" : "Hart",
    "student_id" : "1010"
}

#creates documents in students
kevin_student_id = db.students.insert_one(kh1010).inserted_id
print(f"Inserted student record into the students collection with document_id {kevin_student_id}.")

#prints new document info
print("\n\n-- DISPLAYING STUDENT TEST DOC --")
doc = db.students.find_one({"student_id": "1010"})
fn = doc.get("first_name")
ln = doc.get("last_name")
sid = doc.get("student_id")
print(f"First Name: {fn}")
print(f"Last Name: {ln}")
print(f"Student ID: {sid}")

#deletes new document
db.students.delete_one({"student_id": "1010"})

#displays new results
print("\n\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
docs = db.students.find({})
for doc in docs:
    sid = doc.get("student_id")
    fn = doc.get("first_name")
    ln = doc.get("last_name")
    print(f"Student ID: {sid}")
    print(f"First Name: {fn}")
    print(f"Last Name: {ln}\n")

print("\n\nEnd of Program, press any key to continue...")
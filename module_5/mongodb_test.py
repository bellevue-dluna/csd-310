print("Denae Luna")
print("CSD 310")
print("20 June 2021\n\n")

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.xbgps.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

print("-- Pytech Collection List --")
print(db.list_collection_names())

print("\n\n\tEnd of Program, press any key to exit...")

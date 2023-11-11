from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://Krishnakant:passwordflaskapp@cluster0.wsrp3x5.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["Notesapplication"]

# users = db["users"]

# notes = db["notes"]
# db.users.createIndex( { "user_id": 1 }, { unique: true } )

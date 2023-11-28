from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://leo:1qaz2wsx@cluster0.im14enu.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


test_database = client.test
users_collection = test_database.users

users_collection.insert_one({
    "nane":"leo",
    "gender":"男"
})
print("insert successful")



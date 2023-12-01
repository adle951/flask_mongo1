from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId

uri = "mongodb+srv://leo:1qaz2wsx@cluster0.im14enu.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# 創造或指定 database 跟 collection
test_database = client.test
users_collection = test_database.users

# 新增資料
# result = users_collection.insert_many([{
#     "nane":"leo",
#     "gender":"男"
# }, {"name": "allen",
#     "gender": "男"
# }, {"name": "roey",
#     "gender": "女"
# }])
# print("insert successful")
# print(result.inserted_ids)

# 查詢資料
data = users_collection.find_one()
print(data)

data2 = users_collection.find_one(ObjectId('6569ad8388e89abdc6cacac7'))
print(data2["nane"])

data3 = users_collection.find()
for _ in data3:
    print(_["_id"])
    print(_["gender"])

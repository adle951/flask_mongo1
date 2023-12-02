import pymongo
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
# data = users_collection.find_one()
# print(data)
#
# data2 = users_collection.find_one(ObjectId('6569ad8388e89abdc6cacac7'))
# print(data2["nane"])

# data2 = users_collection.find_one({"name": "roey"})
# print(data2["gender"])

# data3 = users_collection.find()
# for _ in data3:
#     print(_["_id"])
#     print(_["gender"])


# 查詢篩選及排序
result = users_collection.find({
    "$or" : [{"gender" : "女"}, {"gender" : "man"}]},
    sort=[("level", pymongo.ASCENDING )]
)

for doc in result:
    print(doc)


# # 修改一筆資料
# result = users_collection.update_one({
#     "gender" : "男"
# }, { "$set" : { "gender" : "man"
#     }
# })

# # 修改多筆資料
# result = users_collection.update_many({
#     "gender" : "man"
# }, { "$inc" : { "level" : 1
#     }
# })
#
# print(result.matched_count)
# print(result.modified_count)

# 刪除資料
# result = users_collection.delete_many({
#     "nane" : "leo"
# })
#
# print("實際刪除的數量:", result.deleted_count)
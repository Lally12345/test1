import pymongo
client = pymongo.MongoClient("mongodb+srv://Lally:Rali12345@cluster0.smoye81.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={"name":'lally',"email":'lally@gmail.com','surname':'pradhan'}

db1=client['mongodb']
coll=db1['test']
coll.insert_one(d)
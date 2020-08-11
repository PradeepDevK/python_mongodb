import pymongo

mongo_client = pymongo.MongoClient('localhost',27017)

db = mongo_client.myDB
my_collection=db['myFriends']

print('='*50)

#Create/Insert records into mongodb
tom={'name':'Tom','age':38,'sex':'Male','hobbies':['Cooking','Golf','Tennis']}
alice={'name':'Alice','age':39,'sex':'Female','hobbies':['Programming','TV','Motorcycle']}
tom_id=my_collection.insertOne(tom)
alice_id=my_collection.insertOne(alice)
print(tom_id)
print(alice_id)

#Read/Fetch records from mongodb
print("="*25)
cursor=my_collection.find()
print(cursor.count())
for item in cursor:
    print(item)


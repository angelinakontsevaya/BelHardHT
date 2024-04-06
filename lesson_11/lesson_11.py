import pymongo

client = pymongo.MongoClient('localhost',27017)
database = client.users
collection = database.accounts

db_list = client.list_database_names()
if 'user' in db_list:
    print("Yes")
print('No')





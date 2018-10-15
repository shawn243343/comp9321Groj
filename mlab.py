from pymongo import MongoClient


DB_NAME = '93210'
DB_HOST = 'ds163510.mlab.com'
DB_PORT = 63510
DB_USER = '93210'
DB_PASS = 'comp9321'

collection_name = '93210'

dic = {}

client = MongoClient(host=DB_HOST, port=DB_PORT)
db = client[DB_NAME]
db.authenticate(DB_USER, DB_PASS)
c = db[collection_name]
c.insert(dic)

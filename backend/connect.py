# from pymongo import MongoClient

# # Replace with your connection string
# client = MongoClient("mongodb://localhost:27017/") 
# db = client["my_database"]
# collection = db["my_collection"]

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://pedro-user:123@bancosangue.eryecey.mongodb.net/?appName=BancoSangue"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Sucesso na conexão ao MongoDB!")
except Exception as e:
    print("Ocorreu um erro na tentativa de conexão ao MongoDB!")
    print(e)
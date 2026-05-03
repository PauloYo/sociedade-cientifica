from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from os import getenv
from dotenv import load_dotenv
load_dotenv()

uri = getenv("MONGODB_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Sucesso na conexão ao MongoDB!")
except Exception as e:
    print("Ocorreu um erro na tentativa de conexão ao MongoDB!")
    print(e)
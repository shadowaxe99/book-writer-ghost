```python
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from src.utils.data_encryption import encrypt_data, decrypt_data

class MongoDBConnection:
    def __init__(self, host, port, username, password, db_name):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.db_name = db_name
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient(
                host=self.host,
                port=self.port,
                username=self.username,
                password=self.password,
                authSource=self.db_name
            )
            self.db = self.client[self.db_name]
            self.client.admin.command('ismaster')
            print("MongoDB Connection Successful")
        except ConnectionFailure:
            print("MongoDB Connection Failed")
            self.client = None
            self.db = None

    def disconnect(self):
        if self.client is not None:
            self.client.close()
            print("MongoDB Connection Closed")

    def insert_data(self, collection_name, data):
        if self.db is not None:
            encrypted_data = encrypt_data(data)
            collection = self.db[collection_name]
            collection.insert_one(encrypted_data)
            print(f"Data Inserted Successfully into {collection_name}")

    def retrieve_data(self, collection_name, query):
        if self.db is not None:
            collection = self.db[collection_name]
            encrypted_data = collection.find_one(query)
            data = decrypt_data(encrypted_data)
            return data

databaseConfig = {
    "host": "localhost",
    "port": 27017,
    "username": "admin",
    "password": "password",
    "db_name": "ai_interview_db"
}

mongodb_connection = MongoDBConnection(**databaseConfig)
mongodb_connection.connect()
```
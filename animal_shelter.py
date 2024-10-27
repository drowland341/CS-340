from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # MongoDB credentials
        USER = 'aacuser'
        PASS = 'greatpassword'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31944
        DB = 'AAC'
        COL = 'animals'

        # Initialize MongoClient and connect to the database
        self.client = MongoClient(f'mongodb://aacuser:greatpassword@nv-desktop-services.apporto.com:31944/AAC?authSource=admin')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Create method (C in CRUD)
    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)  # Insert document into the collection
                return True
            except Exception as e:
                print(f"Error during insertion: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Read method (R in CRUD)
    def read(self, query):
        if query is not None:
            try:
                result = list(self.collection.find(query))  # Use find() to query multiple documents
                return result  # Return the list of documents
            except Exception as e:
                print(f"Error during querying: {e}")
                return []
        else:
            raise Exception("Query parameter is empty")

    # Update method (U in CRUD)
    def update(self, query, updated_data):
        if query is not None and updated_data is not None:
            try:
                result = self.collection.update_many(query, {'$set': updated_data})  # Update matching documents
                return result.modified_count  # Return the number of documents modified
            except Exception as e:
                print(f"Error during update: {e}")
                return 0
        else:
            raise Exception("Both query and updated data must be provided")

    # Delete method (D in CRUD)
    def delete(self, query):
        if query is not None:
            try:
                result = self.collection.delete_many(query)  # Use delete_many to remove matching documents
                return result.deleted_count  # Return the number of documents deleted
            except Exception as e:
                print(f"Error during deletion: {e}")
                return 0
        else:
            raise Exception("Query parameter is empty")


from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:55299' % (username, password))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):        
        #Put the information gained to the data dictionary
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary  
            return True #Returns true, because data was not none and inserted into the database
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, data):
        data = self.database.animals.find(data)
        if data is not None: #sucessfuly found
            jsonObject = list(data)
            return jsonObject
        else: #not found
            raise Exception("Nothing to find here")
            
# This method is used to read all of the data from a given database
    def readAll(self):
        data = self.database.animals.find({})
        if data is not None:
            jsonObject = list(data)
            return jsonObject
        else:
            raise Exception("Nothing to find here")
            
# This method is used to read all of the data from a given database given limiting values
    def readAllSearch(self, key, value):
        data = self.database.animals.find({key : value})
        if data is not None:
            jsonObject = list(data)
            return jsonObject
        else:
            raise Exception("Nothing to find here")
        
#Create method to impliment the U in CRUD
    def update(self, key, value, newData):
        updateFile = self.database.animals.find({key : value})
        if updateFile is not None: #successfuly found
            self.database.animals.opdate_one(updateFile, newData)
        else: #not found
            raise Exception("Nothing to update: no file was found")
            
#Create method to impliment the D in CRUD
    def delete(self, key, value):
        deleteFile = self.database.animals.find({key : value})
        if deleteFile is not None: #successfuly found
            self.database.animals.delete_one(deleteFile)
        else: #not found
            raise Exception("Nothing to delete: no file was found")
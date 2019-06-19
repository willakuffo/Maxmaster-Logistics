import pickle

def openDB_and_dump(whichDB,data):
    with open(whichDB,'wb') as DB:
            pickle.dump(data,DB)

def openDB_and_load(whichDB):
    with open(whichDB,'rb') as DB:
        data = pickle.load(DB)
        print(data)
        return data

def addnewTruck(truckID):
        pass

openDB_and_dump('truck_ids.pickle',[6,7,8])
openDB_and_load('truck_ids.pickle')

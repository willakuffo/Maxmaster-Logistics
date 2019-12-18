import pickle
class TDB:
        def __int__(self):
                pass
        
        
        def openDB_and_dump(self,whichDB,data):
                with open(whichDB,'wb') as DB:
                        pickle.dump(data,DB)

        def openDB_and_load(self,whichDB):
                with open(whichDB,'rb') as DB:
                        data = pickle.load(DB)
                        print(data)
                        return data

        def addnewTruck(self,truckInfo):
                self.openDB_and_dump('truck_ids.pickle',truckInfo)

#openDB_and_dump('truck_ids.pickle',[6,7,8])
#openDB_and_load('truck_ids.pickle')

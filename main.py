import sqlite3 as sql

class DataBaseHabdler:
    def __init__(self, givenName):
        self.name = givenName
        self.filename = self.name + ".db"

    def connect(self):
        self.connection = sql.connect(self.filename)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.connection.close()

    def createEntity(self, name):
        self.connect()
        self.cursor.execute(f"""CREATE TABLE {name} (
                                ID integer PRIMARY KEY,
                                x text,
                                y text,
                                z integer
                                );""")
        self.disconnect()



    def addRecord(self, entityName, *values):
        self.connect()
        self.cursor.execute(f"""INSERT INTO {entityName} VALUES (?, ...)""", (id, values[0], values[1], ...))
        self.connection.commit()
        self.disconnect()

    def fetchData(self, entityName):
        self.connect()
        self.cursor.execute(f"SELECT * FROM {entityName}")
        result = self.cursor.fetchall()
        self.disconnect()
        return result
    
    def updataRecord(self, entityName, update, condition):
        self.connect()
        self.cursor.execute(f"UPDATE {entityName} SET x=:new WHERE ID=:id", {"new": update, "id": condition})
        self.connection.commit()
        self.disconnect()

    def updataKey(self, newid, id):
        self.connect()
        self.cursor.execute("UPDATE pupils1 SET ID=? WHERE ID=?", (newid, id))
        self.connection.commit()
        self.disconnect()

    def deleteRecord(self, entityName, condition):
        self.connect()
        self.cursor.execute(f"DELETE FROM {entityName} WHERE ID=?", (condition,))
        self.connection.commit()
        self.disconnect()
        self.resetIDs()

    

    def resetIDs(self, entityName):
        self.connect()
        self.cursor.execute("SELECT COUNT(*) FROM pupils1;")
        num_of_records = self.cursor.fetchone()[0]
        
        for row in range(0, num_of_records):
            self.cursor.execute(f"SELECT ID FROM {entityName} LIMIT 1 OFFSET ?", (row, ))
            currentRecord = self.cursor.fetchone()
            if currentRecord[0] != row:
                self.cursor.execute(f"UPDATE {entityName} SET ID=:newid WHERE ID=:currentid", {"newid": row+1, "currentid": currentRecord[0]})

        
        self.connection.commit()  
        self.disconnect()

    def selectRecordByIndex(self, entityName, index):
        self.connect()
        self.cursor.execute(f"SELECT * FROM {entityName} LIMIT 1 OFFSET ?;", (index,))
        result = self.cursor.fetchall()
        self.disconnect()
        return result
         
        

database = DataBaseHabdler("test")

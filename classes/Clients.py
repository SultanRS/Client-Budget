class Client:
    
    def __init__(self, clientID, clientName, engagementID):
        self.clientID = clientID
        self.clientName = clientName
        self.engagementID = engagementID

    def initializeTable():
        # Clients Table
        table = """CREATE TABLE IF NOT EXISTS clients(
               Client_ID TEXT PRIMARY KEY NOT NULL,
               Client_Name TEXT NOT NULL,
               Eng_ID TEXT)"""
        return table

    def getClients():
        query = """SELECT * FROM clients"""
        return query
    
    def findDuplicatedClient(self):
        query = """SELECT Client_ID, Client_Name FROM clients WHERE Client_ID LIKE :clientID AND Client_Name = :clientName"""
        return query
    
    def getMaxClientEntityID(self):
        query = """SELECT Client_ID FROM clients WHERE Client_ID LIKE :clientID"""
        return query

    def addClient(self):
        query = """INSERT INTO clients VALUES (:clientID, :clientName, :engagementID)"""
        return query
    
    def updateClient(self):
        pass
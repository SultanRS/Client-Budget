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

    def addClient(self):
        query = """INSERT INTO clients VALUES (:clientID, :clientName, :engagementID)"""
        return query
    
    def updateClient(self, clientID, clientName, engagementID):
        pass
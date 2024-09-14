class customSolutionBudget:

    def __init__(self, clientID, csID, staffHours, seniorHours, managerHours):
        self.clientID = clientID
        self.csID = csID
        self.staffHours = staffHours
        self.seniorHours = seniorHours
        self.managerHours = managerHours

    def initializeTable():
        # Custom Solution Budgets Table
        table = """CREATE TABLE IF NOT EXISTS cs_budgets(
               Client_ID TEXT PRIMARY KEY NOT NULL,
               CS_ID INTEGER NOT NULL,
               Staff_Hours REAL NOT NULL,
               Senior_Hours REAL NOT NULL,
               Manager_Hours REAL NOT NULL,
               FOREIGN KEY (Client_ID) REFERENCES clients(Client_ID) ON UPDATE CASCADE)"""
        return table

    def generateBudgets(self):
        pass

    def previewBudgets(self):
        pass

    def addBudget(self):
        pass

    def updateBudget(self):
        pass
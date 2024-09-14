class CustomSolution:

    def __init__(self, csID, csName):
        self.csID = csID
        self.csName = csName

    def initializeTable():
        # Custom Solutions Table
        table = """CREATE TABLE IF NOT EXISTS custom_solutions(
               CS_ID INTEGER PRIMARY KEY AUTOINCREMENT,
               CS_Name TEXT NOT NULL)"""
        return table

    def getCustomSolutions(self):
        pass

    def addCustomSolution(self):
        pass

    def updateCustomSolution(self):
        pass
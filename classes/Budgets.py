class Budget:

    def __init__(self, clientID, categoryID, analyzerID, isDownloaded, isDummy):
        self.clientID = clientID
        self.categoryID = categoryID
        self.analyzerID = analyzerID
        self.isDownloaded = isDownloaded
        self.isDummy = isDummy

    def initializeTable():
        # Budgets Table
        table = """CREATE TABLE IF NOT EXISTS budgets(
               Client_ID TEXT PRIMARY KEY NOT NULL,
               Category_ID INTEGER NOT NULL,
               Analyzer_ID INTEGER NOT NULL,
               Is_Downloaded INTEGER NOT NULL DEFAULT 0,
               Is_Dummy INTEGER NOT NULL DEFAULT 0,
               FOREIGN KEY (Client_ID) REFERENCES clients(Client_ID) ON UPDATE CASCADE,
               FOREIGN KEY (Category_ID) REFERENCES categories(Category_ID) ON UPDATE CASCADE,
               FOREIGN KEY (Analyzer_ID) REFERENCES analyzers(Analyzer_ID) ON UPDATE CASCADE)"""
        return table

    def generateBudgets(self):
        pass

    def previewBudgets(self):
        pass

    def addBudget(self):
        pass

    def updateBudget(self):
        pass
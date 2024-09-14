class Tool:

    def __init__(self, analyzerID, tool, toolDescription):
        self.analyzerID = analyzerID
        self.tool = tool
        self.toolDescription = toolDescription

    def initializeTable():
        # Analyzers/Tools Table
        table = """CREATE TABLE IF NOT EXISTS analyzers(
               Analyzer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
               Tool TEXT NOT NULL,
               Tool_Description TEXT NOT NULL)"""
        return table

    def getTools(self):
        pass

    def addTool(self):
        pass

    def updateTool(self):
        pass
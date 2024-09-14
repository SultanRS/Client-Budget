class Category:

    def __init__(self, categoryID, category, categoryDescription, staffHours, seniorHours, managerHours):
        self.categoryID = categoryID
        self.category = category
        self.categoryDescription = categoryDescription
        self.staffHours = staffHours
        self.seniorHours = seniorHours
        self.managerHours = managerHours

    def initializeTable():
        # Categories Table
        table = """CREATE TABLE IF NOT EXISTS categories(
               Category_ID INTEGER PRIMARY KEY AUTOINCREMENT,
               Category TEXT NOT NULL,
               Category_Description TEXT NOT NULL,
               Staff_Hours REAL NOT NULL,
               Senior_Hours REAL NOT NULL,
               Manager_Hours REAL NOT NULL)"""
        return table

    def getCategories(self):
        pass

    def addCategory(self):
        pass

    def updateCategory(self):
        pass
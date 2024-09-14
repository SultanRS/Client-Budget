import sqlite3
from classes import Clients, Categories, Tools, CS_Solutions, Budgets, CS_Budgets
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# User Interface declaration
root = tk.Tk()

# Database connection, creates one if not exists.
connection = sqlite3.connect(".\\database\\Clients_DB.db")
# Enable foreign key support
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor()

# Table initialization
cursor.execute(Clients.Client.initializeTable()) # Clients Table
cursor.execute(Categories.Category.initializeTable()) # Categories Table
cursor.execute(Tools.Tool.initializeTable()) # Analyzers/Tools Table
cursor.execute(CS_Solutions.CustomSolution.initializeTable()) # Custom Solutions Table
cursor.execute(Budgets.Budget.initializeTable()) # Client Budget
cursor.execute(CS_Budgets.customSolutionBudget.initializeTable()) # Custom Solution Budget

def on_closing():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        connection.close() # Closes database
        root.destroy()  # Close the window if the user confirms

def clear_gui():
    # Clear current window
    for widget in root.winfo_children():
        widget.destroy()    

def InsertClientGUI():
    clear_gui()
    def InsertClient():
        value1 = entry_1.get()
        value2 = entry_2.get()
        value3 = entry_3.get()

        client = Clients.Client(value1, value2, value3)

        try:
            cursor.execute(client.addClient(), {"clientID":client.clientID,"clientName":client.clientName,"engagementID":client.engagementID})
            connection.commit()
            messagebox.showinfo("Success", f"INFO: Client successfully created.")
        except sqlite3.IntegrityError:
            connection.rollback()
            messagebox.showinfo("Error", f"ERROR: Client ID: {client.clientID} already exists.")

    root.title("Client Creation")

    tk.Label(root, text="Client ID: ").grid(row=0, column=0, padx=10, pady=10)
    entry_1 = tk.Entry(root)
    entry_1.grid(row=1, column=0, padx=10, pady=10)

    tk.Label(root, text="Client Name: ").grid(row=2, column=0, padx=10, pady=10)
    entry_2 = tk.Entry(root)
    entry_2.grid(row=3, column=0, padx=10, pady=10)

    tk.Label(root, text="Engagement ID: ").grid(row=4, column=0, padx=10, pady=10)
    entry_3 = tk.Entry(root)
    entry_3.grid(row=5, column=0, padx=10, pady=10)

    button_1 = tk.Button(root, text="Create", command=InsertClient)
    button_1.grid(row=6, column=0, padx=10, pady=10)
    button_2 = tk.Button(root, text="Go Back", command=BudgetInterface)
    button_2.grid(row=7, column=0, padx=10, pady=10)

def UpdateClientGUI():
    clear_gui()
    def UpdateClient():
        value1 = entry_1.get()
        value2 = entry_2.get()
        value3 = entry_3.get()

        client = Clients.Client(value1, value2, value3)

        try:
            #cursor.execute(client.updateClient(), {"clientID":client.clientID,"clientName":client.clientName,"engagementID":client.engagementID})
            #connection.commit()
            #connection.close()
            messagebox.showinfo("Success", f"INFO: Client successfully updated.")
        except sqlite3.IntegrityError:
            #connection.rollback()
            #connection.close()
            messagebox.showinfo("Error", f"ERROR: Client ID: {client.clientID} does not exist.")

    root.title("Update Client")
    root.geometry("400x400")

    client_list = cursor.execute(Clients.Client.getClients())
    client_list = client_list.fetchall()

    options = []

    for clients in client_list:
        options.append(f"{clients[0]}|Client Name: {clients[1]}")
        
    dropdown = ttk.Combobox(root, values=options)
    dropdown.set("Select an option")
    dropdown.pack(fill=tk.X, expand=True, padx=10, pady=5)

    tk.Label(root, text="Client ID: ").pack(fill=tk.X, expand=True, padx=10, pady=5)
    entry_1 = tk.Entry(root)
    entry_1.pack(fill=tk.X, expand=True, padx=10, pady=5)

    tk.Label(root, text="Client Name: ").pack(fill=tk.X, expand=True, padx=10, pady=5)
    entry_2 = tk.Entry(root)
    entry_2.pack(fill=tk.X, expand=True, padx=10, pady=5)

    tk.Label(root, text="Engagement ID: ").pack(fill=tk.X, expand=True, padx=10, pady=5)
    entry_3 = tk.Entry(root)
    entry_3.pack(fill=tk.X, expand=True, padx=10, pady=5)

    button_1 = tk.Button(root, text="Update", command=UpdateClient)
    button_1.pack(fill=tk.X, expand=True, padx=10, pady=5)
    button_2 = tk.Button(root, text="Go Back", command=BudgetInterface)
    button_2.pack(fill=tk.X, expand=True, padx=10, pady=5)

def BudgetInterface():
    clear_gui()

    root.title("Client Budget Administration Tool")
    root.geometry("800x600")
    tk.Label(root, text="Client Administration:").pack(padx=10, pady=10)
    button_1 = tk.Button(root, text="Create Client", command=InsertClientGUI)
    button_1.pack(fill=tk.X, expand=True, padx=10, pady=5)
    button_2 = tk.Button(root, text="UpdateClient", command=UpdateClientGUI)
    button_2.pack(fill=tk.X, expand=True, padx=10, pady=5)
    #button_3 = tk.Button(root, text="DeleteClient", command=DeleteClientGUI)
    #button_3.grid(row=0, column=0, padx=10, pady=10)

BudgetInterface()
root.protocol("WM_DELETE_WINDOW", on_closing)
# Initialize Interface
root.mainloop()
import tkinter as tk
from tkinter import simpledialog


class GUI:
    def __init__(self, ctrl):
        self.controller = ctrl
        self.root = tk.Tk()
        self.root.title("Gaming Platforms")
        self.mainMenu()

    def mainMenu(self):
        self.controller.connect()
        menu_frame = tk.Frame(self.root)
        menu_frame.pack()

        tk.Label(menu_frame, text="Select action:").pack()
        tk.Button(menu_frame, text="Work with Games", command=self.gameUI).pack()
        tk.Button(menu_frame, text="Work with DLCs", command=self.dlcUI).pack()
        tk.Button(menu_frame, text="Exit program", command=self.exitProgram).pack()

    def gameUI(self):
        self.controller.showAllGames()

        while True:
            action = simpledialog.askinteger("Action",
                                             "Select action:\n1. Add a game\n2. Delete a game\n3. Back to main menu",
                                             parent=self.root)

            if action == 1:
                Name = simpledialog.askstring("Add Game", "Enter name: ")
                Price = simpledialog.askinteger("Add Game", "Enter price: ")
                ReleaseDate = simpledialog.askstring("Add Game", "Enter release date: ")
                AgeRestriction = simpledialog.askinteger("Add Game", "Enter an age restriction: ")
                GameFileSizeInGB = simpledialog.askinteger("Add Game", "Enter the game file size in GB: ")
                AchievementNumber = simpledialog.askinteger("Add Game", "Enter an achievement number: ")
                self.controller.addGame(Name, Price, ReleaseDate, AgeRestriction, GameFileSizeInGB, AchievementNumber)
            elif action == 2:
                Id = simpledialog.askinteger("Delete Game", "Enter game id: ")
                self.controller.deleteGame(Id)
            elif action == 3:
                break

    def dlcUI(self):
        self.controller.showAllDLCs()

        while True:
            action = simpledialog.askinteger("Action",
                                             "Select action:\n1. Add a DLC\n2. Delete a DLC\n3. Back to main menu",
                                             parent=self.root)

            if action == 1:
                GameId = simpledialog.askinteger("Add DLC", "Enter game id: ")
                Price = simpledialog.askinteger("Add DLC", "Enter price: ")
                Name = simpledialog.askstring("Add DLC", "Enter name: ")
                Description = simpledialog.askstring("Add DLC", "Enter description: ")
                self.controller.addDLC(GameId, Price, Name, Description)
            elif action == 2:
                Id = simpledialog.askinteger("Delete DLC", "Enter DLC id:")
                self.controller.deleteDLC(Id)
            elif action == 3:
                break

    def exitProgram(self):
        self.controller.disconnect()
        self.root.destroy()

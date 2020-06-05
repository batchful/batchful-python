#region modules
import webbrowser, os, shutil

# tkinter modules
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
#endregion

#region variables
# Final variables
filePath = os.path.abspath(__file__) # Includes 'batchful.py'
currentLocation = os.path.dirname(os.path.abspath(__file__)) # Doesn't include 'batchful.py'

# Other variables
xSize = "500"
ySize = "500"
#endregion

#region functions
def PrintLogo():
    print (" _             _         _       __         _ ")
    print ("| |__    __ _ | |_  ___ | |__   / _| _   _ | |")
    print ("| '_ \  / _` || __|/ __|| '_ \ | |_ | | | || |")
    print ("| |_) || (_| || |_| (__ | | | ||  _|| |_| || |")
    print ("|_.__/  \__,_| \__|\___||_| |_||_|   \__,_||_|")

def SubFolders():
    for root, subdirs, files in os.walk(currentLocation):
        files = [f for f in files if not f[0] == '.']
        subdirs[:] = [d for d in subdirs if not d[0] == '.']

        CheckIfEmpty()
        
        for file in files:
            print (root, currentLocation)
            if root != currentLocation:
                path = os.path.join(root, file)
                shutil.move(path, currentLocation)
                    
                CheckIfEmpty()

def CheckIfEmpty():
    for root, subdirs, files in os.walk(currentLocation):
        files = [f for f in files if not f[0] == '.']
        subdirs[:] = [d for d in subdirs if not d[0] == '.']

        if not files:
            os.rmdir(root)   

def ByExt():   
    if sortSubFolders.get() == 1:
        SubFolders()

    for root, subdirs, files in os.walk(currentLocation):
        files = [f for f in files if not f[0] == '.']
        subdirs[:] = []

        for file in files:
            path = os.path.join(root, file)
            fileExtension = os.path.splitext(path)[1]

            if path != filePath:
                if fileExtension != "":
                    folderPath = os.path.join(root, fileExtension)
                else:
                    folderPath = os.path.join(root, "FILE")

                if not os.path.isdir(fileExtension):                
                    os.mkdir(folderPath)
                
                shutil.move(path, folderPath)

def SortByName():
    def GetName():
        ByName(askName.get())

    askWindow = Tk()
    askWindow.title("batchful")
    askWindow.geometry("200x200")

    title = Label(askWindow, text = "Enter A Phrase")
    title.grid(column = 1, row = 0)

    askName = Entry(askWindow, width = 10)
    askName.grid(column = 1, row = 1)

    askButton = Button(askWindow, text = "Search", command = GetName)
    askButton.grid(column = 1, row = 2)

    quitButton = Button(askWindow, text = "Go Back", command = askWindow.destroy)
    quitButton.grid(column = 0, row = 3)

def ByName(name):
    if sortSubFolders.get() == 1:
        SubFolders()


    for root, subdirs, files in os.walk(currentLocation):
        files = [f for f in files if not f[0] == '.']
        subdirs[:] = []

        for file in files:
            path = os.path.join(root, file)
            fileName = os.path.splitext(path)[0]

            if path != filePath:
                folderPath = os.path.join(root, name)

                if not os.path.isdir(name):
                    os.mkdir(folderPath)
                
                if name in fileName:
                    shutil.move(file, folderPath)

def GitHub():
    open = messagebox.askquestion(title = "GitHub", message = "Open GitHub?")
    if open == "yes":
        OpenGitHub()

def OpenGitHub():
    webbrowser.open("https://github.com/batchful/batchful-python")

def Help():
    return
#endregion

#region main loop
window = Tk()
window.title("batchful")
window.geometry(xSize + "x" + ySize)
# window.wm_iconbitmap("Logo.ico")

title = Label(window, text = "batchful", font = ("Ariel Bold", 50))
title.grid(column = 1, row = 0)

extensionButton = Button(window, text = "Sort By Extension", command = ByExt)
extensionButton.grid(column = 0, row = 1)

nameButton = Button(window, text = "Sort By Name", command = SortByName)
nameButton.grid(column = 1, row = 1)

sortSubFolders = IntVar()
sortSubFoldersCheckBox = Checkbutton(window, text = "Search Sub-Folders", var = sortSubFolders)
sortSubFoldersCheckBox.grid(column = 2, row = 1)

helpButton = Button(window, text = "Help", command = Help)
helpButton.grid(column = 1, row = 2)

gitHubButton = Button(window, text = "GitHub", command = GitHub)
gitHubButton.grid(column = 2, row = 2)

quitButton = Button(text = "Quit", command = window.destroy)
quitButton.grid(column = 0, row = 5)

window.mainloop()
#endregion
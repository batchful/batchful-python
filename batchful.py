# Imports modules
import webbrowser, os, shutil
from tkinter import *
from tkinter.ttk import *

# Final variables
filePath = os.path.abspath(__file__) # Includes 'batchful.py'
currentLocation = os.path.dirname(os.path.abspath(__file__)) # Doesn't include 'batchful.py'

# Other variables
xSize = "500"
ySize = "500"

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

def ByName():
    if sortSubFolders.get() == 1:
        SubFolders()

    print ("Enter a phrase:")
    name = input("")

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
    
    print ("Run again? [Y/n]")
    answer = input("")

    if answer == "Y" or answer == "y":
        ByName()

def GitHub():
    print ("Made by 3174N and SFR-git \n")
    print ("Open GitHub? [Y/n] \n")

    answer = input("")

    if answer == "Y" or answer == "y":
        webbrowser.open("https://github.com/batchful/batchful-python")

def Help():
    return

def Ask():
    print ("This program organizes folders. place this file in the directory you wish to organize and run it.")
    print ("Choose a method of organization: \n")
    print ("1. By file extensions.")
    print ("2. By file names.")
    print ("3. Empty sub-folders. \n\n")
    print ("Press g for the GitHub repository page, h for help and q to exit the program. \n")

    answer = input("")

    if answer == "1":
        ByExt()
    elif answer == "2":
        ByName()
    elif answer == "3":
        SubFolders()
    elif answer == "G" or answer == "g":
        GitHub()
    elif answer == "H" or answer == "h":
        Help()

def Exit():
    return
#endregion

# Main loop / code
window = Tk()
window.title("batchful")
window.geometry(xSize + "x" + ySize)

title = Label(window, text = "batchful", font = ("Ariel Bold", 50))
title.grid(column = 1, row = 0)
title.focus()

extensionButton = Button(window, text = "Sort By Extension", command = ByExt)
extensionButton.grid(column = 0, row = 1)

nameButton = Button(window, text = "Sort By Name", command = ByName)
nameButton.grid(column = 1, row = 1)

sortSubFolders = IntVar()
sortSubFoldersCheckBox = Checkbutton(window, text = "Search Sub-Folders", var = sortSubFolders)
sortSubFoldersCheckBox.grid(column = 2, row = 1)

window.mainloop()
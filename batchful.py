#region modules
import webbrowser, os, shutil

# tkinter modules
try:
    # For python 3+
    from tkinter import *
    from tkinter.ttk import *
    from tkinter import messagebox
except:
    # For python 2+
    from Tkinter import *
    from ttk import *
    import tkMessageBox as messagebox
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
def combineFuncs(*funcs):
    def combinedFunc(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combinedFunc

def SubFolders():
    for root, subdirs, files in os.walk(currentLocation):
        files = [f for f in files if not f[0] == '.']
        subdirs[:] = [d for d in subdirs if not d[0] == '.']

        CheckIfEmpty()
        
        for file in files:
            print (root, currentLocation)
            if (root != currentLocation):
                path = os.path.join(root, file)
                shutil.move(path, currentLocation)
                    
                CheckIfEmpty()

def CheckIfEmpty():
    for root, subdirs, files in os.walk(currentLocation):
        files = [f for f in files if not f[0] == '.']
        subdirs[:] = [d for d in subdirs if not d[0] == '.']

        if (not files):
            os.rmdir(root)   

def ByExt():   
    if (sortSubFolders.get() == 1):
        SubFolders()

    for root, subdirs, files in os.walk(currentLocation):
        files = [f for f in files if not f[0] == '.']
        subdirs[:] = []

        count = 0

        for file in files:
            path = os.path.join(root, file)
            fileExtension = os.path.splitext(path)[1]

            if (path != filePath):
                if (fileExtension != ""):
                    folderPath = os.path.join(root, fileExtension)
                else:
                    folderPath = os.path.join(root, "FILE")

                if (not os.path.isdir(fileExtension)):                
                    os.mkdir(folderPath)
                
                shutil.move(path, folderPath)
                count += 1
    
    messagebox.showinfo(title = "batchful", message = "Moved " + str(count) + " File(s)")

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

    askButton = Button(askWindow, text = "Search", command = combineFuncs(GetName, askWindow.destroy))
    askButton.grid(column = 1, row = 2)

    quitButton = Button(askWindow, text = "Go Back", command = askWindow.destroy)
    quitButton.grid(column = 0, row = 3)

def ByName(name):
    if (sortSubFolders.get() == 1):
        SubFolders()


    for root, subdirs, files in os.walk(currentLocation):
        files = [f for f in files if not f[0] == '.']
        subdirs[:] = []

        count = 0

        for file in files:
            path = os.path.join(root, file)
            fileName = os.path.splitext(path)[0]

            if (path != filePath):
                folderPath = os.path.join(root, name)

                if (not os.path.isdir(name)):
                    os.mkdir(folderPath)
                
                if (name in fileName):
                    shutil.move(file, folderPath)
                    count += 1
    
    messagebox.showinfo(title = "batchful", message = "Moved " + str(count) + " File(s)")

def GitHub():
    open = messagebox.askquestion(title = "GitHub", message = "Open GitHub?")
    if (open == "yes"):
        OpenGitHub()

def OpenGitHub():
    webbrowser.open("https://github.com/batchful/batchful-python")

#region help
def Help():
    helpWindow = Tk()
    helpWindow.title("batchful - help")

    helpText = Label(helpWindow, text = "HOW TO USE BATCHFUL:", font = ("Ariel Bold", 25))
    helpText2 = Label(helpWindow, text = "In the main screen, choose a method of organization.\n\
Currently, there are 2 methods of organization: \n\
1. By file extension: creates a directory for every filetype \n\
    and sorts the files accordingly. \n\
2. By file name: creates a directory for a spacefic phrase and moves \n\
    all of the files containing the phrase to the directory. \n\
\n\
You will also be presented with the option to sort through subfolders. \n\
This process deletes the unnecessary folders after it's done sorting. \n\
\n\
To run the program, just press the desired button. \n\
you can make sub-folders search active by checking the checkbox", font = ("Ariel", 15))

    
    backButton = Button(helpWindow, text = "Go Back", command = helpWindow.destroy)
    currentLocationLabel = Label(helpWindow, text = "Current location: " + str(currentLocation), font = ("Ariel 12"))
    
    helpText.grid(column = 0, row = 0)
    helpText2.grid(column = 0, row = 1)
    currentLocationLabel.grid(column = 0, row = 3)
    backButton.grid(column = 0, row = 4)

    placeholder = Label(helpWindow).grid(column = 0, row = 2)
#endregion
#endregion

#region main loop
window = Tk()
window.title("batchful")
window.geometry(xSize + "x" + ySize)
# window.wm_iconbitmap("Logo.ico")
# window.tk_setPalette("black")

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
helpButton.grid(column = 0, row = 3)

gitHubButton = Button(window, text = "GitHub", command = GitHub)
gitHubButton.grid(column = 1, row = 3)

quitButton = Button(text = "Quit", command = window.destroy)
quitButton.grid(column = 2, row = 5)

placeholder = Label(window).grid(column = 0, row = 2)
placeholder2 = Label(window).grid(column = 0, row = 4)

window.mainloop()
#endregion
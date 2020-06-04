import webbrowser, os, shutil, tkinter


filePath = os.path.abspath(__file__) # Includes 'batchful.py'
currentLocation = os.path.dirname(os.path.abspath(__file__)) # Doesn't include 'batchful.py'

batchfulLogo = " _             _         _       __         _ \n| |__    __ _ | |_  ___ | |__   / _| _   _ | |\n| '_ \  / _` || __|/ __|| '_ \ | |_ | | | || |\n| |_) || (_| || |_| (__ | | | ||  _|| |_| || |\n|_.__/  \__,_| \__|\___||_| |_||_|   \__,_||_|"

def SubFolders():
    for root, subdirs, files in os.walk(currentLocation):
        files = [f for f in files if not f[0] == '.']
        subdirs[:] = [d for d in subdirs if not d[0] == '.']

        for file in files:
            if root != currentLocation:
                path = os.path.join(root, file)
                shutil.move(path, currentLocation)
    
        for subdir in subdirs:
            path = os.path.join(root, subdir)
            os.rmdir(path)

    Ask()

def ByExt():        
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

print (batchfulLogo)
Ask()

def Exit():
    return
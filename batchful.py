import webbrowser, os, shutil, tkinter

currentLocation = os.path.abspath(__file__)

batchfulLogo = " _             _         _       __         _ \n| |__    __ _ | |_  ___ | |__   / _| _   _ | |\n| '_ \  / _` || __|/ __|| '_ \ | |_ | | | || |\n| |_) || (_| || |_| (__ | | | ||  _|| |_| || |\n|_.__/  \__,_| \__|\___||_| |_||_|   \__,_||_|"

def ByExt():        
    print (currentLocation)

    fileName, fileExtension = os.path.splitext(currentLocation)
    print (fileName)
    print (fileExtension)

def ByName():
    return

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
    print ("2. By file names. \n \n")
    print ("Press g for the GitHub repository page, h for help and q to exit the program. \n")

    answer = input("")

    if answer == "1":
        ByExt()
    elif answer == "2":
        ByName()
    elif answer == "G" or answer == "g":
        GitHub()
    elif answer == "H" or answer == "h":
        Help()

print (batchfulLogo)
Ask()
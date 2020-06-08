# region modules
import webbrowser
import os
import shutil

# Tries to import kivy
try:
    from kivy.app import App
    from kivy.uix.widget import Widget
    from kivy.uix.screenmanager import ScreenManager, Screen
    from kivy.properties import ObjectProperty
    from kivy.lang import Builder
    from kivy.uix.popup import Popup
    from kivy.uix.label import Label

    usingKivy = True
except:
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

    usingTkinter = True
# endregion

# region variables
# Final variables
filePath = os.path.abspath(__file__)  # Includes 'batchful.py'
currentLocation = os.path.dirname(os.path.abspath(__file__))  # Doesn't include 'batchful.py'

# Other variables
xSize = "500"
ySize = "500"

if usingKivy:
    usingTkinter = False
elif usingTkinter:
    usingKivy = False
else:
    print("ERROR: MODULES NOT IMPORTED CORRECTLY")
# endregion

# region kivy setup
if usingKivy:
    class MainWindow(Screen):
        def by_ext_button(self):
            by_ext()


    class NameWindow(Screen):
        phrase = ObjectProperty(None)

        def by_name_button(self):
            by_name(self.phrase.text)

    class WindowManager(ScreenManager):
        pass


    def show_moved_files(num):
        pop = Popup(title="batchful",
                    content=Label(text="Moved " + str(num) + " File(s)"),
                    size_hint=(None, None), size=(200, 200))
        pop.open()

    kv = Builder.load_file("batchful.kv")


    class batchfulApp(App):
        def build(self):
            return kv


# endregion

# region functions
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return combined_func


def sub_folders(name, extension):
    for root, subdirs, files in os.walk(currentLocation):
        files = [f for f in files if not f[0] == '.']
        subdirs[:] = [d for d in subdirs if not d[0] == '.']

        for file in files:
            path = os.path.join(root, file)
            file_name = os.path.splitext(path)[0]
            if name in file_name:
                if root != currentLocation and path != filePath:
                    print(file)
                    shutil.move(path, currentLocation)

        check_if_empty()


def empty_sub_folders():
    for root, subdirs, files in os.walk(currentLocation):
        files = [f for f in files if not f[0] == '.']
        subdirs[:] = [d for d in subdirs if not d[0] == '.']

        check_if_empty()

        for file in files:
            print(root, currentLocation)
            if root != currentLocation:
                path = os.path.join(root, file)
                shutil.move(path, currentLocation)

                check_if_empty()


def check_if_empty():
    for root, subdirs, files in os.walk(currentLocation):
        files = [f for f in files if not f[0] == '.']
        subdirs[:] = [d for d in subdirs if not d[0] == '.']

        if not files:
            os.rmdir(root)


def by_ext():
    if usingTkinter:
        if sortSubFolders.get() == 1:
            empty_sub_folders()

    for root, subdirs, files in os.walk(currentLocation):
        files = [f for f in files if not f[0] == '.']
        subdirs[:] = []

        count = 0

        for file in files:
            path = os.path.join(root, file)
            file_extension = os.path.splitext(path)[1]

            if path != filePath and file != "batchful.kv":
                if file_extension != "":
                    folder_path = os.path.join(root, file_extension)
                else:
                    folder_path = os.path.join(root, "FILE")

                if not os.path.isdir(file_extension):
                    os.mkdir(folder_path)

                shutil.move(path, folder_path)
                count += 1

    if usingTkinter:
        messagebox.showinfo(title="batchful", message="Moved " + str(count) + " File(s)")
    elif usingKivy:
        show_moved_files(count)


def sort_by_name():
    def get_name():
        by_name(ask_name.get())

    ask_window = Tk()
    ask_window.title("batchful")
    ask_window.geometry("200x200")

    title = Label(ask_window, text="Enter A Phrase")
    title.grid(column=1, row=0)

    ask_name = Entry(ask_window, width=10)
    ask_name.focus()
    ask_name.grid(column=1, row=1)

    ask_button = Button(ask_window, text="Search", command=combine_funcs(get_name, ask_window.destroy))
    ask_button.grid(column=1, row=2)

    quit_button = Button(ask_window, text="Go Back", command=ask_window.destroy)
    quit_button.grid(column=0, row=3)


def by_name(name):
    if usingTkinter:
        if sortSubFolders.get() == 1:
            sub_folders(name, None)

    for root, subdirs, files in os.walk(currentLocation):
        files = [f for f in files if not f[0] == '.']
        subdirs[:] = []

        count = 0
        for file in files:

            path = os.path.join(root, file)
            file_name = os.path.splitext(path)[0]

            if path != filePath and file != "batchful.kv":
                folder_path = os.path.join(root, name)
                if not os.path.isdir(name):
                    if not os.path.isfile(name):
                        os.mkdir(folder_path)
                    else:
                        temp_folder_path = os.path.join(root, "TEMP FOLDER")
                        if not os.path.isdir(temp_folder_path) and not os.path.isfile(temp_folder_path):
                            os.mkdir(temp_folder_path)

                        shutil.move(path, temp_folder_path)
                        print("YAY")
                        path = os.path.join(path, temp_folder_path)
                        if not os.path.isfile(name):
                            os.mkdir(folder_path)

                        shutil.move(path, folder_path)

                        count += 1

                if name in file_name:
                    shutil.move(path, folder_path)
                    count += 1

    if usingTkinter:
        messagebox.showinfo(title="batchful", message="Moved " + str(count) + " File(s)")
    elif usingKivy:
        show_moved_files(count)


def git_hub():
    open = messagebox.askquestion(title="GitHub", message="Open GitHub?")
    if open == "yes":
        open_git_hub()


def open_git_hub():
    webbrowser.open("https://github.com/batchful/batchful-python")


def help():
    help_window = Tk()
    help_window.title("batchful - help")

    help_text = Label(help_window, text="HOW TO USE BATCHFUL:", font=("Ariel Bold", 25))
    help_text2 = Label(help_window, text="In the main screen, choose a method of organization.\n\
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
you can make sub-folders search active by checking the checkbox", font=("Ariel", 15))

    back_button = Button(help_window, text="Go Back", command=help_window.destroy)
    current_location_label = Label(help_window, text="Current location: " + str(currentLocation), font=("Ariel 12"))

    help_text.grid(column=0, row=0)
    help_text2.grid(column=0, row=1)
    current_location_label.grid(column=0, row=3)
    back_button.grid(column=0, row=4)

    place_holder = Label(help_window).grid(column=0, row=2)
# endregion


# region main loop
if usingKivy:
    batchfulApp().run()
elif usingTkinter:
    window = Tk()
    window.title("batchful")
    window.geometry(xSize + "x" + ySize)
    # window.wm_iconbitmap("Logo.ico")
    # window.tk_setPalette("black")

    title = Label(window, text="batchful", font=("Ariel Bold", 50))
    title.grid(column=1, row=0)

    extensionButton = Button(window, text="Sort By Extension", command=by_ext)
    extensionButton.grid(column=0, row=1)

    nameButton = Button(window, text="Sort By Name", command=sort_by_name)
    nameButton.grid(column=1, row=1)

    sortSubFolders = IntVar()
    sortSubFoldersCheckBox = Checkbutton(window, text="Search Sub-Folders", var=sortSubFolders)
    sortSubFoldersCheckBox.grid(column=2, row=1)

    helpButton = Button(window, text="Help", command=help)
    helpButton.grid(column=0, row=3)

    gitHubButton = Button(window, text="GitHub", command=git_hub)
    gitHubButton.grid(column=1, row=3)

    quitButton = Button(text="Quit", command=window.destroy)
    quitButton.grid(column=2, row=5)

    placeholder = Label(window).grid(column=0, row=2)
    placeholder2 = Label(window).grid(column=0, row=4)

    window.mainloop()
# endregion

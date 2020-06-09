*Maintained by [@3174N](https://github.com/3174N)*

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/embersandsgamestudios)
# batchful
A simple and easy-to use Python directory organizer. 

No installation needed, just run `batchful.exe` / `batchful.py`.

## Usage
Paste the program in the directory you wish to organize and run it.

### Dependencies
To run batchful, the following dependencies are needed: 
* `Python 3.7.3` (Should also work on older / newer versions)
  * Upstream: [Official site](https://www.python.org/downloads/)
  * for Ubuntu-based distributions: 
    ```bash
    $ sudo apt install software-properties-common
    $ sudo add-apt-repository ppa:deadsnakes/ppa
    $ sudo apt update
    $ sudo apt install python3.7
    ```
  * for Arch-based distributions: [`python`](https://www.archlinux.org/packages/extra/x86_64/python/)<sup>AUR</sup>
  * for Fedora/RedHat: `sudo dnf install python3 -y`
* `kivy` (Necessary for GUI)
  * Upstream: [Official site](https://kivy.org/#download)
  * On Windows:
    ```commandline
    > python -m pip install kivy
    > python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*
    > python -m pip install kivy_deps.gstreamer==0.1.*
    
    #  for python 3.5 and up:
    > python -m pip install kivy_deps.angle==0.1.*
    ```
  * for Ubuntu-based distributions: 
    ```bash
    $ sudo add-apt-repository ppa:kivy-team/kivy  
    $ sudo apt update
    $ sudo apt-get install python3-kivy
    ```
  * For Debian-based distributions:
  
    Add `deb http://ppa.launchpad.net/kivy-team/kivy/ubuntu xenial main` to `/etc/apt/sources.list`
    ```bash
      $ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A863D2D6
      $ sudo apt update
      $ sudo apt install python3-kivy
      ```
  
  * **NOTE:** If kivy is not installed, batchful will use tkinter as GUI

### Configuration
There are currently two implemented methods of organization: 
1. By file extension: creates a directory for every filetype and sorts the files accordingly. 
2. By file name: creates a directory for a specific phrase and moves all of the files containing it to the directory.

You will also be presented with the option to sort through subfolders.
This process deletes the unnecessary folders after it's done sorting.

Press the button with the desired function to start.

## Coming Soon
- Light theme

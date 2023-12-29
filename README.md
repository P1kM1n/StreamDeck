# Stream Deck

Stream Deck is a customizable button interface for your computer, controlled by a Raspberry Pi (or whatever you want).

## Overview

This project consists of two main components:
- `server.py`: The server script runs on your computer and listens for signals sent by the Stream Deck client.
- `client.py`: The client script runs on a Raspberry Pi, creating a GUI with buttons that, when pressed, send signals to the server to perform various actions.

## Prerequisites

- Python 3.x
- Tkinter (for the client GUI)

## Getting Started

1. Clone the repository:
   Clone the repository onto both the computer you want the applications to be opened on and the device that will be running the GUI
   ``git clone https://github.com/your-username/StreamDeck.git``

2. Navigate to the project directory
 
3. Update the server IP address:
  Open client.py using a text editor of your choice (e.g., Notepad, VSCode).
  On the client device open client.py and replace '192.168.1.21' with the IP address of your computer.

NOTE from this point on, if you open the programs on the right devices and have the same programs as me the code will work. Anything past here is just for customising the programs that open.
  
5. Add/Modify Actions (Customize to Launch Your Applications):
  On the server device (the one you want the applications to open on) open server.py using a text editor of your choice (e.g., Notepad, VSCode).
  Locate the section with the actions for opening programs(``open_1``, ``open_2``, etc.).

  Replace the existing actions with your desired applications. For example, if you want to launch Photoshop, replace ``'open_1': subprocess.run(["C:\\Program Files\\Adobe\\Adobe Photoshop\\Photoshop.exe"]).``
  Save the file.

5. Customize the icons:
On your client device replace the icons in the Icons folder with your preferred icons. Unsurprisingly you will need to change the file references in the code of client.py.

6. Running the program:
   Open client.py on your client device (probably a pi or something similar) and open server.py on your main computer.

This project was made assuming you have some sort of screen next to your main setup, whether that be running off a pi or an actual pc. But tbh since this runs on pretty much anything(even a potato if it could interpret python) you can run it however you want. This also acts as a good scaffhold for a bunch of other projects I might explore in the future.

If this project gains any sort of traction I'll modify the code to be much more user friendly.

If you want me to attach a photo of how I had this setup or just improve this readme in general, just ask (I'm aware how shit this readme is lmao)
Good luck and happy coding :)

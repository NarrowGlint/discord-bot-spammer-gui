from tkinter import *
import sys
import subprocess
import os
from time import sleep

print('Note: This program will only work.')

#Important Stuff

with open('pythoncommand.txt') as f:
    temp = f.read().splitlines()

pythonCommand = temp[0]

proxy_number = 0
proxy_list = []
userToken = open("tokens.txt").read().splitlines()

for token in userToken:
    proxy_list.append('localhost')

#tkinter Window

window = None
window = Tk()
window.title("Discord Bot Spammer")
window.configure(background="white")

#Option Menu

tkvar = StringVar(window)

choices = {'Text Spammer', 'Image Spammer'}
tkvar.set('Text Spammer')

popupMenu = OptionMenu(window, tkvar, *choices)
Label(window, text="Type Of Spammer").grid(row=0, column=0)
popupMenu.grid(row = 1, column =0)

option = 'Text Spammer'
def change_dropdown(*args):
    global option
    option = tkvar.get()
    print(option + ' Selected')


tkvar.trace('w', change_dropdown)

#Discord Server

link = None

def click():
    global link
    link = discordEntry.get()
    print('Link: ' + link)        
    for token in userToken:
        p = subprocess.Popen([pythonCommand, 'executables/joiner.py', token, link, proxy_list[proxy_number]])

Label(window, text="Last Numbers Of Discord Invite | ONLY CLICK JOIN IF YOU HAVENT BEFORE", bg="black", fg="white", font='none 10 bold').grid(row=2, column=0, sticky=W)

discordEntry = Entry(window, width=35, bg="white")
discordEntry.grid(row=3, column=0, sticky=W)

Button(window, text="Join", width=6, command=click).grid(row=3, column=1, sticky=W)

#Text to spam

spam_text = None

def sendtext():
    global spam_text
    spam_text = textentry.get()
    print("Spam Text: " + spam_text)

Label(window, text="Spam Text/Directory To Image", bg='black', fg='white', font='none 10 bold').grid(row=4, column=0, sticky=W)

textentry = Entry(window, width=35, bg='white')
textentry.grid(row=5, column=0, sticky=W)

Button(window, text="Submit", width=6, command=sendtext).grid(row=5, column=1, sticky=W)

# Functions

def start():

    if (option == 'Text Spammer'):
        for token in userToken:
            p = subprocess.Popen([pythonCommand,'executables/textspam.py', token, spam_text, 'null'])
    elif (option == 'Image Spammer'):
        pass



Button(window, text="Start", width=6, command=start, font='none 15 bold').grid(row=8, column=0, sticky=W)

#Stop Button

def stop():
    os.system('taskkill /F /IM python.exe /T')

Button(window, text="Stop", width=6, command=stop, font='none 15 bold').grid(row=8, column=1, sticky=W)

print('Once you have clicked start and everything has loaded, send a message in a channel to start the spam.')

window.mainloop()

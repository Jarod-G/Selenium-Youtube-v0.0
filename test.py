from tkinter import *
import tkinter as tk
import api_youtube as vidFinder

# create the application
myapp = Tk()

#
# window manager
#
myapp.title("VidFinder")
myapp.geometry('600x600')

searchLabel = Label(myapp, text="Enter a word or a sentence and it will give you the first result ").grid(row=0, column=0)
search = StringVar()
searchEntry = Entry(myapp, textvariable=search).grid(row=0, column=1)

#
# interface
#
button = tk.Button(myapp, text='Submit', command=vidFinder.vidfinder(search))

# start the program
myapp.mainloop()
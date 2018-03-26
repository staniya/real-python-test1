from easygui import *

msgbox("Hello, EasyGUI!", "This is a message box", "Hi there")

choices = (["Blue", "Yellow", "Auugh!"])

buttonbox("What is your favorite color?", "Choose wisely...", choices)

title = "Choose wisely..." #window title

indexbox("What is your favorite color?", title, choices)

choicebox("What is your favorite color?", title, choices)

multchoicebox("What is your favorite color?", title, choices)

enterbox("What is your favorite color?", title, choices)

passwordbox("What is your favorite color? (I won't tell.)", title)

textbox("Please describe your favorite color:")

fileopenbox("message", "title", "*.txt")

fileopenbox(title = "Open a file...", default = "*.txt")

#there is also diropenbox() that opens a folder and filesavebox() that allows user to select a file to be saved
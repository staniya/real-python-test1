from easygui import *

message = msgbox("whatcha doing", "This is a message box", "Nothing")
print(message)

choices = ["random", "random2", "random3"]
button = buttonbox("Hello there", "This is a button box", choices)
print(button)

choices2 = ["random", "random2", "random3"]
multiple_choice_box = multchoicebox("Pick an item", "item picker", choices2)
print(multiple_choice_box)

path = "/Users/staniya/Documents/Starting-Project-HTML/Cube-Project/img_next_button_theme_default.png"
index = indexbox("Shall I continue", "wowza", ["Yes", "No"], path)
print(index)

enter = enterbox("Enter something", "wowza", "")
print(enter)

password = passwordbox("Enter your password", "Don't worry no one can see this", "")
print(password)

text = textbox("Message", "Title", "")
print(text)

print(help(indexbox))
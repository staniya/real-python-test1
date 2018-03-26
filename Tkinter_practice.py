from tkinter import *
from tkinter import filedialog


my_app = Tk()

greeting = Label(text="Hello, Tkinter")  # create a text label
greeting.pack()  # add the label to the window

my_app.mainloop()


# ------------------------------------------------------------------------------

# define the GUI application
class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)


# create the application
#window
window = Tk()
window.geometry("400x200")  # default window size

my_app = App(window)
my_app.master.title("I made a window!")
my_app.mainloop()  # start the application

# ------------------------------------------------------------------------------

window = Tk()
window.title("Here's a window")
window.geometry("250x100")  # default window size

my_frame = Frame()
my_frame.pack()

# a bar to span across the entire top

label_text1 = Label(my_frame, text="I've been framed!",
                    bg="red", fg="yellow")

label_text1.pack(fill=X)

# three side-by-side labels
label_left = Label(my_frame, text="left", bg="yellow")
label_left.pack(side=LEFT)  # place label to the left of the next widget

label_mid = Label(my_frame, text="middle", bg="green")
label_mid.pack(side=LEFT)

label_right = Label(my_frame, text="right", bg="blue")
label_right.pack()

window.mainloop()

# ------------------------------------------------------------------------------

window = Tk()
window.geometry("300x200")

button1 = Button(window, text="I'm at offset (50,60)")
button2 = Button(window, text="I'm at offset (0,0)")

button1.pack()
button2.pack()

button1.place(height=200, width=200, x=50, y=65)
button2.place(height=150, width=150, x=0, y=0)

window.mainloop()

# ------------------------------------------------------------------------------

window = Tk()
window.geometry("200x50")

# create sidy-by-side frames
frame_left = Frame(bd=3, relief=SUNKEN)  # give the frame an outline
frame_left.place(relx=0, relwidth=0.5, relheight=1)

frame_right = Frame(bd=3, relief=SUNKEN)
frame_right.place(relx=0.7, relwidth=0.3)

# add a label to each frame
left_label = Label(frame_left, text="I've been framed")
left_label.pack()

right_label = Label(frame_right, text="So have I")
right_label.pack()

window.mainloop()

# ------------------------------------------------------------------------------

window = Tk()

my_frame = Frame()
my_frame.grid()  # add frame to take up the whole window using grid()

label_top_left = Label(my_frame, text="I'm at (1,1)")
label_top_left.grid(row=1, column=1)

label_bottom_left = Label(my_frame, text="I'm at (2,1)")
label_bottom_left.grid(row=2, column=1)

button_bottom_right = Button(my_frame, text="I'm at (3,2)")
button_bottom_right.grid(row=3, column=2)

window.mainloop()  # start the application

# ------------------------------------------------------------------------------

window = Tk()

my_frame = Frame()
my_frame.grid()  # add frame to window using grid()

label_top_left = Label(my_frame, text="I'm at (1,1)", bd="3",
                       relief=SUNKEN)
label_top_left.grid(row=1, column=1, padx=100, pady=30)

label_bottom_left = Label(my_frame, text="I'm at (2,1)", bd="3",
                          relief=SUNKEN)
label_bottom_left.grid(row=2, column=1, sticky=E)

button_right = Button(my_frame, text="I span 2 rows", height=5)
button_right.grid(row=1, column=2, rowspan=2)

window.mainloop()

# ------------------------------------------------------------------------------

window = Tk()


def increment_button():
    new_number = 1 + my_button.cget("text")
    my_button.config(text=new_number)


my_button = Button(text=1, command=increment_button)
my_button.pack()

window.mainloop()  # start the application

# ------------------------------------------------------------------------------

window = Tk()

entry1 = Entry()
entry1.pack()
entry1.insert(0, "this is an entry")

entry2 = Entry()
entry2.pack()

my_text = entry1.get()  # get the text from entry1
entry2.insert(0, my_text)
entry2.insert(8, " also")  # add 'also; to the middle of my_text

window.mainloop()  # start the application


# ------------------------------------------------------------------------------

def recalc():
    cel_temp = entry_cel.get()  # get temp from text entry
    try:  # calculate converted temperature and place it in label
        far_temp = float(cel_temp) * 9 / 5 + 32
        far_temp = round(far_temp, 3)  # round to three decimal places
        result_far.config(text=far_temp)
    except ValueError:  # user entered non-numeric temperature
        result_far.config(text="invalid")


# create the application window and add a Frame
window = Tk()
window.title("Temperature converter")

frame = Frame()
frame.grid(padx=5, pady=5)  # pad top and left of frame 5 pixels before grid

# create and add text labels
label_cel = Label(frame, text="Celsius temperature:")
label_cel.grid(row=1, column=1, sticky=S + E)

label_far = Label(frame, text="Fahrenheit temperature:")
label_far.grid(row=2, column=1, sticky=S + E)

# create and add space for user entry of text
entry_cel = Entry(frame, width=7)
entry_cel.grid(row=1, column=2)
entry_cel.insert(0, 0)

# create and label for text calculation result
result_far = Label(frame)
result_far.grid(row=2, column=2)

# create and add 'recalculate' button
btn_recalc = Button(frame, text="Recalculate", command=recalc)
btn_recalc.grid(row=1, column=3, rowspan=2)

recalc()  # fill in first default temperature conversion

window.mainloop()  # start the application

# ------------------------------------------------------------------------------

window = Tk()

frame = Frame()
frame.pack()


def open_file():  # ask user to choose a file and update label
    type_list = [("Python scripts", "*.py"), ("Text files", "*.txt")]
    file_name = filedialog.askopenfilename(filetypes=type_list)
    label_file.config(text=file_name)


# blank label to hold name of chosen file
label_file = Label(frame)
label_file.pack()

# button to click on for 'Open' file dialog
button_open = Button(frame, text="Choose a file...", command=open_file)
button_open.pack()

window.mainloop()  # start the application

# ------------------------------------------------------------------------------

window = Tk()

frame = Frame()
frame.pack()


def save_file():  # ask user to choose a file and update label
    type_list = [("Python scripts", "*.py"), ("Text files", "*.txt")]
    file_name = filedialog.asksaveasfilename(filetypes=type_list, defaultextension=".py")
    my_text = "I will save:" + file_name
    label_file.config(text=my_text)


# blank label to hold name of chosen file
label_file = Label(frame)
label_file.pack()

# button to click on for 'open' file dialog
button_open = Button(frame, text="Choose a file...", command=save_file)
button_open.pack()

window.mainloop()  # start the application

# ------------------------------------------------------------------------------

def calculate():
    value = right_box.get()
    try:
        my_value = " " + value
        calc_box.config(text=my_value)
    except ValueError:  # user entered non-numeric temperature
        calc_box.config(text="invalid")


window = Tk()
window.title("Grid Right to Left")

frame = Frame()
frame.grid(padx=5, pady=5)

right_box = Entry(frame, width=12)
right_box.grid(row=1, column=3, sticky=S + E)
right_box.insert(0, "Enter a number:")

left_box = Label(frame, text="The value you entered was:")
left_box.grid(row=1, column=1, sticky=S + E)

calc_box = Label(frame)
calc_box.grid(row=1, column=2, sticky=S + E)

btn_calc = Button(frame, text="Calculate", command=calculate)
btn_calc.grid(row=1, column=4, rowspan=2)

window.mainloop()

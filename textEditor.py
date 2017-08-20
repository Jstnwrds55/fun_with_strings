from tkinter import *
from tkinter import filedialog


def openFile():
    text.delete(1.0, END)
    file1 = filedialog.askopenfile(filetypes=[('Text files', '*.txt')])
    contents = file1.read()
    text.insert('1.0', contents)


def saveAs():
    t = text.get("1.0", "end-1c")
    saveLocation = filedialog.asksaveasfilename()
    file1 = open(saveLocation, "w+")
    file1.write(t)
    file1.close()


def fontHelvetica():
    global text
    text.config(font="Helvetica")


def fontCourier():
    global text
    text.config(font="Courier")

# Window Creation Stuff
root = Tk('Text Editor')  # Initialize window
root.wm_title('Text Editor')  # Name window
text = Text(root)  # Use root window as text box
text.grid()  # Initialize grid of text box from root

# Save button stuff
saveButton = Button(root, text="Save", command=saveAs)  # Create save button with saveAs function as command
saveButton.grid()  # Display button

# Load button stuff
openButton = Button(root, text="Load", command=openFile)  # Creates open button with openFile function as command
openButton.grid()

# Font stuff
font = Menubutton(root, text="Font")  # Adds a button that says Font
font.grid()  # Displays the font button
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu
helvetica = IntVar()
courier = IntVar()
font.menu.add_checkbutton(label="Courier", variable=courier,
command=fontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica,
command=fontHelvetica)

root.mainloop()  # Keep window open

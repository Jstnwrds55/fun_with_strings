from tkinter import *
from tkinter import filedialog


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

# Button stuff
button = Button(root, text="save", command=saveAs)  # Create button from root reads save and command is saveAs function
button.grid()  # Display button

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

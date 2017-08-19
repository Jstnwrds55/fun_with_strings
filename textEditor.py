from tkinter import *
from tkinter import filedialog


def saveAs():
    t = text.get("1.0", "end-1c")
    saveLocation = filedialog.asksaveasfilename()
    file1 = open(saveLocation, "w+")
    file1.write(t)
    file1.close()

root = Tk('Text Editor')  # Initialize and name window
text = Text(root)  # Use root window as text box
text.grid()  # Initialize grid of text box from root
button = Button(root, text="save", command=saveAs)  # Create button from root that reads save and command is saveAs function
button.grid()  # Display button

root.mainloop()  # Keep window open

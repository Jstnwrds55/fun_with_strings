from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def open_file():
    if text.get("1.0", "end-1c") != '':
        quit_answer = messagebox.askquestion('Save?', 'Do you want to save this document before loading another one?')
        if quit_answer == 'yes':
            save_as()
    filename = filedialog.askopenfilename(filetypes=[
        ('Python code files', '*.py'),
        ('Perl code files', '*.pl;*.pm'),  # semicolon trick
        ('Java code files', '*.java'),
        ('C++ code files', '*.cpp;*.h'),   # semicolon trick
        ('Text files', '*.txt'),
        ('All files', '*'), ])
    file1 = open(filename)
    text.delete(1.0, END)
    contents = file1.read()
    text.insert(1.0, contents)
    root.wm_title(filename)


def save_as():
    t = text.get("1.0", "end-1c")
    if root.wm_title() == 'Text Editor':
        save_location = filedialog.asksaveasfilename()
        file1 = open(save_location, "w+")
        file1.write(t)
        file1.close()
        root.wm_title(save_location)
    else:
        save_location = root.wm_title()
        file1 = open(save_location, "w+")
        file1.write(t)
        file1.close()


def new_file():
    if text.get("1.0", "end-1c") != '':
        quit_answer = messagebox.askquestion('Save?', 'Do you want to save this document before creating a new one?')
        if quit_answer == 'yes':
            save_as()
    text.delete(1.0, END)


def on_closing():
    if text.get("1.0", "end-1c") != '':
        quit_answer = messagebox.askyesnocancel('Save?', 'Do you want to save this document before exiting?')
        print(quit_answer)
        if quit_answer == True:
            save_as()
            root.destroy()
        elif quit_answer == False:
            root.destroy()
    else:
        root.destroy()


def font_helvetica():
    global text
    text.config(font="Helvetica")


def font_courier():
    global text
    text.config(font="Courier")

# Window Creation Stuff
root = Tk()  # Initialize window
root.wm_title('Text Editor')  # Name window
text = Text(root)  # Use root window as text box
text.grid()  # Initialize grid of text box from root

# Create frame for buttons to fit in
button_frame = Frame(root)
button_frame.grid(row=2, column=0, columnspan=2)

# Save button stuff
save_button = Button(button_frame, text="Save File", command=save_as)  # Create save button with saveAs function as command
save_button.grid(row=0, column=0)  # Display button

# Load button stuff
open_button = Button(button_frame, text="Open File", command=open_file)  # Creates open button with open_file function as command
open_button.grid(row=0, column=1)

# New button stuff
new_button = Button(button_frame, text="New File", command=new_file)
new_button.grid(row=0, column=2)

# Font stuff
font = Menubutton(root, text="Font")  # Adds a button that says Font
font.grid()  # Displays the font button
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu
helvetica = IntVar()
courier = IntVar()
font.menu.add_checkbutton(label="Courier", variable=courier,
command=font_courier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica,
command=font_helvetica)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()  # Keep window open

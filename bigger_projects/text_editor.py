from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def new_file():
    if text.get("1.0", "end-1c") != '':
        quit_answer = messagebox.askquestion('Save?', 'Do you want to save this document before creating a new one?')
        if quit_answer == 'yes':
            save_as()
    text.delete(1.0, END)


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


def save_file():
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


def save_as():
    t = text.get("1.0", "end-1c")
    save_location = filedialog.asksaveasfilename()
    file1 = open(save_location, "w+")
    file1.write(t)
    file1.close()
    root.wm_title(save_location)


def on_closing():
    if text.get("1.0", "end-1c") != '':
        quit_answer = messagebox.askyesnocancel('Save?', 'Do you want to save this document before exiting?')
        if quit_answer:
            save_as()
            root.destroy()
        elif not quit_answer:
            root.destroy()
    else:
        root.destroy()


def about_me():
    messagebox._show('Created by', 'Created by Justin Edwards in Python for fun.')


def font_helvetica():
    selected_text_start = text.index("sel.first")
    selected_text_end = text.index("sel.last")
    try:
        text.tag_add("Helvetica", selected_text_start, selected_text_end)
    except:
        pass
    text.config(font="Helvetica")


def font_courier():
    global text
    text.config(font="Courier")


def font_bold():
    selected_text_start = text.index("sel.first")
    selected_text_end = text.index("sel.last")
    try:
        text.tag_add("Bold", selected_text_start, selected_text_end)
    except:
        pass

# Window Creation Stuff
root = Tk()  # Initialize window
root.wm_title('Text Editor')  # Name window
text = Text(root)  # Use root window as text box
text.grid()  # Initialize grid of text box from root

# Text initialization stuff
text.tag_configure("Helvetica", font="Helvetica")
text.tag_configure("Bold", font="bold")

# Initialize menus
menu = Menu(root)
root.config(menu=menu)

# Create file menu
file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File", command=new_file)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save File", command=save_file)
file_menu.add_command(label="Save As", command=save_as)

# Create font decoration menu
font_menu = Menu(menu)
font_family = Menu(menu)
font_style = Menu(menu)
menu.add_cascade(label="Font", menu=font_menu)

font_menu.add_cascade(label="Choose Font", menu=font_family)
font_family.add_command(label="Helvetica", command=font_helvetica)
font_family.add_command(label="Courier", command=font_courier)
font_menu.add_cascade(label="Font Weight", menu=font_style)
font_style.add_cascade(label="Bold", command=font_bold)

# Create help menu
help_menu = Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about_me)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()  # Keep window open

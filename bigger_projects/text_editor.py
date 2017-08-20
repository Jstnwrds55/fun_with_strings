from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from tkinter.colorchooser import askcolor


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


def font_changer(font_choice):
    text.config(font=(font_choice, 14, style_combo))
    global current_font
    current_font = font_choice


def font_size_changer(size):
    text.config(font=(current_font, size, style_combo))
    global current_font_size
    current_font_size = size


def font_style_changer(option_clicked):
    global is_bold
    global is_italic
    global style_combo
    if option_clicked == 'bold':
        if not is_bold:
            is_bold = True
        else:
            is_bold = False
    elif option_clicked == 'italic':
        if not is_italic:
            is_italic = True
        else:
            is_italic = False
    if is_bold and is_italic:
        style_combo = 'bold italic'
    elif is_bold:
        style_combo = 'bold'
    elif is_italic:
        style_combo = 'italic'
    else:
        style_combo = ''

    text.config(font=(current_font, 14, style_combo))


def color_chooser():
    user_color = askcolor()[1]
    text.config("Color", foreground=user_color)


# If I ever try to change selection again
# selected_text_start = text.index("sel.first")
# selected_text_end = text.index("sel.last")
# text.tag_add("Color", selected_text_start, selected_text_end)
# text.tag_configure("Helvetica", font="Helvetica")

# Window Creation Stuff
root = Tk()  # Initialize window
root.wm_title('Text Editor')  # Name window
text = Text(root)  # Use root window as text box
text.grid()  # Initialize grid of text box from root
text.config(font=('Helvetica', 14))

# Font info
current_font = 'Helvetica'
current_font_size = 14
is_bold = False
is_italic = False
style_combo = ''

root.grid_columnconfigure(0, weight=1)  # Make window stay the same when font changes
text.pack(expand=True, fill='both')  # Text box resizes with window

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
menu.add_cascade(label="Font", menu=font_menu)

font_family = Menu(menu)
font_menu.add_cascade(label="Choose Font", menu=font_family)
fontVar = IntVar(root)
fontVar.set(1)
font_family.add_checkbutton(label="Helvetica", variable=fontVar, command=lambda: font_changer('Helvetica'))
font_family.add_checkbutton(label="Courier", command=lambda: font_changer('Courier'))

font_style = Menu(menu)
font_menu.add_cascade(label="Font Weight", menu=font_style)
font_style.add_checkbutton(label="Bold", command=lambda: font_style_changer('bold'))
font_style.add_checkbutton(label="Italic", command=lambda: font_style_changer('italic'))

font_size = Menu(menu)
sizes_list = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
var = tk.IntVar()
var.set(12)
font_size_options = OptionMenu(root, var, *sizes_list)
font_size_options.pack()
font_menu.add_cascade(label="Font Size", command=font_size_options.pack())
font_color = Menu(menu)
font_menu.add_command(label="Font Color", command=color_chooser)

# Create help menu
help_menu = Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about_me)

root.protocol("WM_DELETE_WINDOW", on_closing)


root.mainloop()  # Keep window open

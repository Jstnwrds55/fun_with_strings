from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from tkinter.colorchooser import askcolor


def new_file(*args):
    if text.get("1.0", "end-1c") != '':
        quit_answer = messagebox.askquestion('Save?', 'Do you want to save this document before creating a new one?')
        if quit_answer == 'yes':
            save_as()
    text.delete(1.0, END)


def open_file(*args):
    if text.get("1.0", "end-1c") != '':
        quit_answer = messagebox.askquestion('Save?', 'Do you want to save this document before loading another one?')
        if quit_answer == 'yes':
            save_as()
    filename = filedialog.askopenfilename(filetypes=[
        ('Python code files', '*.py'),
        ('Perl code files', '*.pl;*.pm'),  # semicolon trick
        ('Java code files', '*.java'),
        ('C++ code files', '*.cpp;*.h'),  # semicolon trick
        ('Text files', '*.txt'),
        ('All files', '*'), ])
    file1 = open(filename)
    text.delete(1.0, END)
    contents = file1.read()
    text.insert(1.0, contents)
    root.wm_title(filename)


def save_file(*args):
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


def save_as(*args):
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
        elif quit_answer is None:
            pass
        elif not quit_answer:
            root.destroy()
    else:
        root.destroy()


def about_me():
    messagebox._show('Created by', 'Created by Justin Edwards in Python for fun.')


def font_changer(font_choice):
    text.config(font=(font_choice, current_font_size, style_combo))
    global current_font
    current_font = font_choice


def font_size_changer(clicked_size):
    global current_font_size
    current_font_size = clicked_size
    text.config(font=(current_font, current_font_size, style_combo))


def font_style_changer(*args):
    global style_combo
    style_combo = (is_bold.get() + ' ' + is_italic.get() + ' ' + is_underline.get())
    text.config(font=(current_font, current_font_size, style_combo))


def color_chooser():
    user_color = askcolor()[1]
    text.config(foreground=user_color)


# If I ever try to change selection again
# selected_text_start = text.index("sel.first")
# selected_text_end = text.index("sel.last")
# text.tag_add("Color", selected_text_start, selected_text_end)
# text.tag_configure("Helvetica", font="Helvetica")

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

if __name__ == "__main__":
    # Window Creation Stuff
    root = Tk()  # Initialize window
    root.wm_title('Text Editor')  # Name window
    root.wm_geometry('700x400')
    text = Text(root)  # Use root window as text box
    text.grid(row=0, column=0, sticky='nsew')  # Initialize grid of text box from root
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    text.config(font=('Helvetica', 14))

    # Font info
    current_font_size = 12
    current_font = 'Helvetica'
    style_combo = []

    # root.grid_columnconfigure(0, weight=1)  # Make window stay the same when font changes
    # text.grid()  # Text box resizes with window

    # Initialize menus
    menu = Menu(root)
    root.config(menu=menu)

    # Create file menu
    file_menu = Menu(menu)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New File", command=new_file, accelerator="Command+N")
    file_menu.add_command(label="Open File", command=open_file, accelerator="Command+O")
    file_menu.add_command(label="Save File", command=save_file, accelerator="Command+S")
    file_menu.add_command(label="Save As", command=save_as, accelerator="Command+Shift+S")
    root.bind('<Command-n>', new_file)
    root.bind('<Command-o>', open_file)
    root.bind('<Command-s>', save_file)
    root.bind('<Command-Shift-s>', save_as)

    # Create font decoration menu
    font_menu = Menu(menu)
    menu.add_cascade(label="Font", menu=font_menu)

    # Font family dropdown
    font_family = Menu(menu)
    font_menu.add_cascade(label="Choose Font", menu=font_family)
    font_family.add_radiobutton(label="Helvetica", value=1, command=lambda: font_changer('Helvetica'))
    font_family.add_radiobutton(label="Courier", command=lambda: font_changer('Courier'))

    # Font style dropdown
    font_style = Menu(menu)
    font_menu.add_cascade(label="Font Weight", menu=font_style)
    is_bold = tk.StringVar()
    font_style.add_checkbutton(label="Bold", variable=is_bold, onvalue='bold', offvalue='', command=font_style_changer,
                               accelerator="Command+B")
    is_italic = tk.StringVar()
    font_style.add_checkbutton(label="Italic", variable=is_italic, onvalue='italic', offvalue='',
                               command=font_style_changer, accelerator="Command+I")
    is_underline = tk.StringVar()
    font_style.add_checkbutton(label="Underline", variable=is_underline, onvalue='underline', offvalue='',
                               command=font_style_changer, accelerator='Command+U')

    root.bind('<Command-B>', font_style_changer)
    root.bind('<Command-i>', font_style_changer)
    root.bind('<Command-u>', font_style_changer)

    # Font size dropdown
    font_size = Menu(menu)
    font_menu.add_cascade(label="Font Size", menu=font_size)
    font_size.add_command(label=str(8), command=lambda: font_size_changer(8))
    font_size.add_command(label=str(12), command=lambda: font_size_changer(12))
    font_size.add_command(label=str(16), command=lambda: font_size_changer(16))
    font_size.add_command(label=str(20), command=lambda: font_size_changer(20))
    font_size.add_command(label=str(24), command=lambda: font_size_changer(24))
    font_size.add_command(label=str(28), command=lambda: font_size_changer(28))
    font_size.add_command(label=str(32), command=lambda: font_size_changer(32))
    font_size.add_command(label=str(36), command=lambda: font_size_changer(36))
    font_size.add_command(label=str(40), command=lambda: font_size_changer(40))
    font_size.add_command(label=str(44), command=lambda: font_size_changer(44))

    # Color chooser
    font_color = Menu(menu)
    font_menu.add_command(label="Font Color", command=color_chooser)

    # Create help menu
    help_menu = Menu(menu)
    menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=about_me)

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()  # Keep window open

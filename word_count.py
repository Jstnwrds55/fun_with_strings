from tkinter import Tk
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.withdraw()
messagebox.showinfo("Word Count", "Choose the .txt file with words you want to count.")
file_path = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])


def word_counter(text):
    word_list = text.split(' ')
    print('The document you selected contained ' + str(len(word_list)) + ' words!')
    return(len(word_list))

word_counter(open(file_path).read())

from tkinter import Tk
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.withdraw()
messagebox.showinfo("Word Count", "Choose the .txt file with words you want to count.")
file_path = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])


def wordCounter(text):
    wordList = text.split(' ')
    print('The document you selected contained ' + str(len(wordList)) + ' words!')
    return(len(wordList))

wordCounter(open(file_path).read())

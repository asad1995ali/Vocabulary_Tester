# OBJECTIVE: a gui program that displays a word and asks for meaning #
import random
from tkinter import *
from pandas import *


# take data from excel file and return value to text field
def word_generator(a):
    df = pandas.read_excel('Vocabulary.xlsx', sheet_name='Sheet1')
    words = df['Word'].tolist()
    meanings = df['Meaning'].tolist()

    if a == 1:
        t1.delete(1.0, END)
        t2.delete(1.0, END)
        t1.insert(END, words[random.randint(0, len(words))])

    if a == 2:
        t2.delete(1.0, END)
        t2.insert(END, meanings[words.index(str(t1.get(1.0, END)).rstrip("\n"))])


# GUI Setup
window = Tk()

b1 = Button(window, text="Worte", command=lambda: word_generator(1))
b2 = Button(window, text="Bedeutung", command=lambda: word_generator(2))
b1.grid(row=3, column=1, rowspan=2)
b2.grid(row=3, column=3, rowspan=2)

t2 = Text(window, height=2, width=30)
t2.grid(row=1, column=3, rowspan=2)

t1 = Text(window, height=2, width=30)
t1.grid(row=1, column=1, rowspan=2)

window.mainloop()
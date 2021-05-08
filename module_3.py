#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb


def insert_text():
    file_name = fd.askopenfilename()
    try:
        f = open(file_name)
        s = f.read()
        text.insert(1.0, s)
        f.close()
    except(FileNotFoundError, TypeError):
        mb.showinfo("Открытие файла",
                    "Файл не выбран!")


def extract_text():
    file_name = fd.asksaveasfilename(
        filetypes=(("TXT files", "*.txt"),
                   ("HTML files", "*.html;*.htm"),
                   ("All files", "*.*")))
    try:
        f = open(file_name, 'w')
        s = text.get(1.0, END)
        f.write(s)
        f.close()
    except(FileNotFoundError, TypeError):
        mb.showinfo("Сохранение файла",
                    "Фаил не сохранен!")


def delete_text():
    answer = mb.askyesno("Удаление", "Удалить данные?")
    if answer:
        text.delete(1.0, END)


root = Tk()

text = Text(width=50, height=25)
text.grid(columnspan=3)
bt1 = Button(text="Открыть", command=insert_text)
bt1.grid(row=1, sticky=E)
bt2 = Button(text="Сохранить", command=extract_text)
bt2.grid(row=1, column=1, sticky=W)
bt3 = Button(text="Очистить", command=delete_text)
bt3.grid(row=1, column=2, sticky=E)
root.mainloop()

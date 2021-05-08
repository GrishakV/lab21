#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *


class Paint:
    def __init__(self, main, func):
        self.c = Canvas(
            main,
            width=600,
            height=600,
            bg='white'
        )
        self.bt1 = Button(
            main,
            text='Добавить фигуру'
        )
        self.bt1['command'] = eval('self.' + func)
        self.c.grid()
        self.bt1.grid()

    def new_window(self):
        def create(event):
            x1 = int(en1.get())
            y1 = int(en2.get())
            x2 = int(en3.get())
            y2 = int(en4.get())
            if r_var.get() == 0:
                self.c.create_rectangle(x1, y1, x2, y2, width=2)
            elif r_var.get() == 1:
                self.c.create_oval(x1, y1, x2, y2, width=2)

        a = Toplevel()
        a.title('Фигура')
        a.resizable(False, False)
        a.geometry('125x125')
        lb1 = Label(a, text='x1')
        lb2 = Label(a, text='y1')
        lb3 = Label(a, text='x2')
        lb4 = Label(a, text='y2')
        en1 = Entry(a, width=5)
        en2 = Entry(a, width=5)
        en3 = Entry(a, width=5)
        en4 = Entry(a, width=5)

        r_var = BooleanVar()
        r_var.set(0)
        r1 = Radiobutton(a, text="Прямоугольник", variable=r_var, value=0)
        r2 = Radiobutton(a, text="Овал", variable=r_var, value=1)
        bt2 = Button(a, text="Нарисовать")
        bt2.bind('<Button-1>', create)

        lb1.grid(row=0, column=0)
        en1.grid(row=0, column=1)
        lb2.grid(row=0, column=2)
        en2.grid(row=0, column=3)
        lb3.grid(row=1, column=0)
        en3.grid(row=1, column=1)
        lb4.grid(row=1, column=2)
        en4.grid(row=1, column=3)
        r1.grid(row=2, column=0, columnspan=4, sticky=W)
        r2.grid(row=3, column=0, columnspan=4, sticky=W)
        bt2.grid(row=4, column=0, columnspan=4)


if __name__ == '__main__':
    root = Tk()
    root.title("Прямовал")
    main_window = Paint(root, 'new_window')
    root.mainloop()

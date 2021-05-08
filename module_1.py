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
        self.c.pack()
        self.bt1.pack()

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
        a.geometry('200x150')
        f1 = Frame(a)
        f2 = Frame(a)
        f3 = Frame(a)
        f1.pack()
        f2.pack()
        f3.pack()
        lb1 = Label(f1, text='x1')
        lb2 = Label(f1, text='y1')
        lb3 = Label(f2, text='x2')
        lb4 = Label(f2, text='y2')
        en1 = Entry(f1, width=5)
        en2 = Entry(f1, width=5)
        en3 = Entry(f2, width=5)
        en4 = Entry(f2, width=5)
        lb1.pack(side=LEFT)
        en1.pack(side=LEFT)
        lb2.pack(side=LEFT)
        en2.pack(side=LEFT)
        lb3.pack(side=LEFT)
        en3.pack(side=LEFT)
        lb4.pack(side=LEFT)
        en4.pack(side=LEFT)

        r_var = BooleanVar()
        r_var.set(0)
        r1 = Radiobutton(f3, text="Прямоугольник", variable=r_var, value=0)
        r2 = Radiobutton(f3, text="Овал", variable=r_var, value=1)
        bt2 = Button(f3, text="Нарисовать")
        bt2.bind('<Button-1>', create)

        r1.pack(anchor=W)
        r2.pack(anchor=W)
        bt2.pack()


if __name__ == '__main__':
    root = Tk()
    root.title("Прямовал")
    main_window = Paint(root, 'new_window')
    root.mainloop()

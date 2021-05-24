#!/usr/bin/env python3
# -*- config: utf-8 -*-


# Вариант 12. Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона;
# дата рождения (список из трех чисел). Написать программу, выполняющую следующие
# действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть размещены по алфавиту; вывод на экран информации о людях, чьи
# дни рождения приходятся на месяц, значение которого введено с клавиатуры; если таких
# нет, выдать на дисплей соответствующее сообщение.


from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import ind1module


def add_window():
    def add():
        brd = str(en3.get())
        name = en1.get()
        phone = en2.get()
        birthday = list(map(int, brd.split(',')))

        people.add(name, phone, birthday)

    add_w = Toplevel()
    add_w.title('Добавить')
    add_w.resizable(False, False)
    add_w.geometry('225x100')
    en1 = Entry(add_w)
    en2 = Entry(add_w)
    en3 = Entry(add_w)
    lb1 = Label(add_w, text="ФИО")
    lb2 = Label(add_w, text="Номер")
    lb3 = Label(add_w, text="Дата рождения")
    bt1 = Button(add_w, text="Добавить", command=add)

    lb1.grid(row=0, column=0)
    lb2.grid(row=1, column=0)
    lb3.grid(row=2, column=0)
    en1.grid(row=0, column=1)
    en2.grid(row=1, column=1)
    en3.grid(row=2, column=1)
    bt1.grid(row=3, column=0, columnspan=2)


def load_window():
    file_name = fd.askopenfilename()
    try:
        f = open(file_name)
        people.load(file_name)
        f.close()
    except(FileNotFoundError, TypeError):
        mb.showinfo("Открытие файла",
                    "Файл не выбран!")


def save_window():
    try:
        file_name = fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("XML files", "*.xml"),
                       ("All files", "*.*")))
        f = open(file_name, 'w')
        f.write('')
        f.close()
        people.save(file_name)
    except(FileNotFoundError, TypeError):
        mb.showinfo("Сохранение файла",
                    "Файл не выбран!")


def help_window():
    help_w = Toplevel()
    help_w.title('ТЕБЕ НИЧЕГО УЖЕ НЕ ПОМОЖЕТ')
    help_w.resizable(False, False)
    help_w['bg'] = 'white'
    img = PhotoImage(file='wolf.png')
    bt2 = Button(
        help_w,
        image=img,
        bg='white',
        borderwidth=0,
        activebackground='white',
        command=lambda: help_w.destroy()
    )
    bt2.image = img
    bt2.pack()


def select_window():
    def choice():
        try:
            choice_en = int(en4.get())
            res = people.select(choice_en)
            if res:
                for idx, person in enumerate(res, 1):
                    text.delete(0.0, END)
                    text.insert(0.0, '{:>4}: {}'.format(idx, person.name))
            else:
                text.delete(0.0, END)
                text.insert(0.0, 'В этом месяце именинников нема')
        except(ValueError, TypeError):
            mb.showinfo("Выбор месяца",
                        "Введите месяц!")

    sel_w = Toplevel()
    sel_w.title('Выбрать')
    sel_w.resizable(False, False)
    sel_w.geometry('225x100')
    lb4 = Label(sel_w, text="Введите месяц")
    en4 = Entry(sel_w)
    bt3 = Button(sel_w, text="Подтвердить", command=choice)
    lb4.pack(padx=2, pady=2)
    en4.pack(padx=2, pady=2)
    bt3.pack(padx=2, pady=2)


def show():
    text.delete(0.0, END)
    text.insert(0.0, people)


if __name__ == '__main__':
    people = ind1module.People()

    root = Tk()
    root.geometry('800x450')
    root.title('Главное окно')
    root.resizable(False, False)

    main_menu = Menu(root)
    root.config(menu=main_menu)

    file_menu = Menu(main_menu, tearoff=0)
    file_menu.add_command(label="Открыть", command=load_window)
    file_menu.add_command(label="Добавить", command=add_window)
    file_menu.add_command(label="Сохранить", command=save_window)

    main_menu.add_cascade(label="Файл", menu=file_menu)
    main_menu.add_command(label="Показать", command=show)
    main_menu.add_command(label="Выбрать", command=select_window)
    main_menu.add_command(label="Помощь", command=help_window)
    main_menu.add_command(label="Выход", command=lambda: root.destroy())

    text = Text(bg='white', width=97, height=100)
    text.pack(side=LEFT)
    scroll = Scrollbar(command=text.yview)
    scroll.pack(side=LEFT, fill=Y)
    text.config(yscrollcommand=scroll.set)

    root.mainloop()

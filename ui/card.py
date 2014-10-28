# -*- coding: utf-8 -*-

import ttk
from Tkinter import *
import tkMessageBox


class Card(ttk.Frame):
    def __init__(self, master=None, **kw):
        ttk.Frame.__init__(self, master, **kw)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.subject = ttk.Label(self, font=('Arial', 20))
        self.subject.grid(column=0, row=0, columnspan=3)

        self.answer = ttk.Label(self, font=('Arial', 10))
        self.answer.grid(column=0, row=1, columnspan=2)

        ttk.Style().configure('TLabel', padding=10)

        self.btn_correct = ttk.Button(self, text='Good', command=self.action_correct)
        self.btn_correct.grid(column=0, row=2, sticky='nsew')
        self.btn_correct.grid_remove()

        self.btn_wrong = ttk.Button(self, text='Bad', command=self.action_wrong)
        self.btn_wrong.grid(column=1, row=2, sticky='nsew')
        self.btn_wrong.grid_remove()

        self.btn_show = ttk.Button(self, text='Show', command=self.show_answer)
        self.btn_show.grid(column=0, row=2, columnspan=2, sticky='nsew')

        self.item = None
        self.queue = None

    def action_correct(self):
        self.queue.correct()
        self.next_prompt()

    def action_wrong(self):
        self.queue.incorrect()
        self.next_prompt()

    def show_answer(self):
        self.answer.config(text=self.item.details)
        self.btn_show.grid_remove()
        self.btn_correct.grid()
        self.btn_wrong.grid()

    def next_prompt(self):
        self.item = self.queue.next()
        if self.item:
            self.answer.config(text='')
            self.subject.config(text=self.item.subject)
            self.btn_show.grid()
            self.btn_correct.grid_remove()
            self.btn_wrong.grid_remove()
        else:
            tkMessageBox.showinfo(message='No more cards!', parent=self.master)
            self.master.master.deiconify()
            self.master.destroy()
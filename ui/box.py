# -*- coding: utf-8 -*-

import ttk
from Tkinter import *


class Box(ttk.Frame):
    def sample(self, id):
        if self.callback:
            self.callback(id)

    def __init__(self, master=None, **kw):
        ttk.Frame.__init__(self, master, **kw)

        self.callback = None
        self.buttons = []
        for i in range(6):
            b = ttk.Button(self, text=str(i+1), command= (lambda i=i+1: self.sample(i)))

            c = 0
            if (i+1) % 3 == 2:
                c = 1
            elif (i+1) % 3 == 0:
                c = 2

            r = 0
            if i > 2:
                r = 1

            b.grid(column=c, row=r, sticky='nsew')

            self.buttons.append(b)

        c, r = self.grid_size()

        for i in range(c):
            self.grid_columnconfigure(i, weight=1)

        for i in range(r):
            self.grid_rowconfigure(i, weight=1)




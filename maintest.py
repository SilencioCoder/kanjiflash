# -*- coding: utf-8 -*-

import ttk
from Tkinter import *
from lib.queue import *
from lib.storage import *
import tkMessageBox


def test_box(app):
    import ui.box
    import ui.card

    s = Storage()
    s.source = 'kanjiflash.db'

    p = Queue()
    p.storage = s

    app.box = ui.box.Box(app)

    def temp(id):
        p.initialize(id)
        if p.queue:
            app.withdraw()

            view = Toplevel(app)
            view.geometry('{}x{}'.format(250, 150))
            view.grid_columnconfigure(0, weight=1)
            view.grid_rowconfigure(0, weight=1)
            view.card = ui.card.Card(view)
            view.card.queue = p
            view.card.next_prompt()
            view.card.grid(column=0, row=0, sticky='nsew')

            def callback():
                app.deiconify()
                view.destroy()

            view.protocol('WM_DELETE_WINDOW', callback)
        else:
            tkMessageBox.showinfo(message='There no cards in this box!', parent=app)

    app.box.callback = temp
    app.box.grid(column=0, row=0, sticky='nsew')

def test_card(app):
    import ui.card
    app.card = ui.card.Card(app)
    app.card.grid(column=0, row=0, sticky='nsew')

if __name__ == '__main__':
    app = Tk()
    app.grid()

    test_box(app)

    app.geometry('{}x{}'.format(250, 150))
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)
    app.resizable(True, False)
    app.mainloop()

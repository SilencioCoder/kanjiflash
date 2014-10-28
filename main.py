# -*- coding: utf-8 -*-

import ttk
from Tkinter import *
from lib.queue import Queue
from ui.box import Box
from ui.card import Card


def get_source():
    source = [
        {'kanji': '後', 'kana': 'あと', 'eng': 'afterwards'},
        {'kanji': '買い物', 'kana': 'かいもの', 'eng': 'shopping'},
        {'kanji': '行く', 'kana': 'いく', 'eng': 'to go'}
    ]
    return source


if __name__ == '__main__':
    app = Tk()
    app.grid()
    app.geometry('{}x{}'.format(250, 150))
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)
    app.resizable(False, False)
    app.mainloop()

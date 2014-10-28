# -*- coding: utf-8 -*-

from lib.info import Info
import sqlite3


class Storage(object):
    def __init__(self):
        self.source = ''

    def retrieve(self, box):
        conn = sqlite3.connect(self.source)

        c = conn.cursor()
        result = c.execute('SELECT * FROM item WHERE box=?', (box, ))

        l = []
        for i in result:
            s = Info()
            s.id = i[0]
            s.subject = i[1]
            s.details = i[2]
            s.mastery = i[3]
            l.append(s)

        conn.close()

        return l

    def save(self, subject):
        conn = sqlite3.connect(self.source)

        c = conn.cursor()
        c.execute('UPDATE item SET box = ? WHERE id = ?', (subject.mastery, subject.id))
        conn.commit()
        conn.close()

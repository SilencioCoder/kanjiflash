# -*- coding: utf-8 -*-

from random import shuffle


class Queue(object):
    def __init__(self):
        self.min = 1
        self.max = 6
        self.item = None
        self.queue = None
        self.storage = None

    def initialize(self, level):
        self.queue = self.storage.retrieve(level)
        shuffle(self.queue)

    def next(self):
        if self.queue:
            self.item = self.queue.pop()
            return self.item
        return None

    def correct(self):
        if self.item.mastery < self.max:
            self.item.mastery += 1
            self.storage.save(self.item)

    def incorrect(self):
        if self.item.mastery > self.min:
            self.item.mastery -= 1
            self.storage.save(self.item)

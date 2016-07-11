# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 21:17:48 2016

@author: Jieqiong Liu
"""

from treap import Treap

class MedianFinder:
    def __init__(self):
        self.treap = Treap()
        self.histogram = {}

    def addItem(self, item):
        if item > 0:
            self.treap.insert(item)
            self.histogram[item] = self.histogram.get(item, 0) + 1

    def delItem(self, item):
        if item > 0:
            self.treap.delete(item)
            self.histogram[item] -= 1

    def updateItem(self, item, delta):
        self.delItem(item)
        self.addItem(item+delta)

    def findMedian(self):
        return self.treap.median()

#!/usr/bin/python
#########################################################################
# Author: Jieqiong Liu
# Created Time: 2016-07-10 23:07:14
# File Name: ./treap.py
# Description:
#########################################################################

import random

class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.size = 1
        self.ran = random.random()

    def updateSize(self):
        self.size = 1
        if self.left is not None:
            self.size += self.left.size
        if self.right is not None:
            self.size += self.right.size

    def __str__(self):
        if self.left is not None:
            x = str(self.left)
        else:
            x = ''
        if self.right is not None:
            y = str(self.right)
        else:
            y = ''
        return '((%d,%d) L%s R%s)'%(self.val, self.size, x, y)

def getSize(x):
    if x is None:
        return 0
    else:
        return x.size

class Treap():

    def __init__(self):
        self.root = None

    def leftRot(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        x.updateSize()
        y.updateSize()
        return y

    def rightRot(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        x.updateSize()
        y.updateSize()
        return y

    def __insert(self, node, val):
        if node is None:
            return TreeNode(val)
        if val < node.val:
            node.left = self.__insert(node.left, val)
            if node.left.ran < node.ran:
                return self.rightRot(node)
        else:
            node.right = self.__insert(node.right, val)
            if node.right.ran < node.ran:
                return self.leftRot(node)
        node.updateSize()
        return node

    def insert(self, val):
        self.root = self.__insert(self.root, val)

    def __merge(self, left, right):
        if left is None:
            return right
        elif right is None:
            return left
        elif left.ran < right.ran:
            left.right = self.__merge(left.right, right)
            left.updateSize()
            return left
        else:
            right.left = self.__merge(left, right.left)
            right.updateSize()
            return right

    def __delete(self, node, val):
        if node.val == val:
            return self.__merge(node.left, node.right)
        elif val < node.val:
            node.left = self.__delete(node.left, val)
            node.updateSize()
        else:
            node.right = self.__delete(node.right, val)
            node.updateSize()
        return node

    def delete(self, val):
        self.root = self.__delete(self.root, val)

    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.size

    def __findKth(self, node, k):
        lcnt = getSize(node.left)
        if lcnt == k - 1:
            return node.val
        elif lcnt >= k:
            return self.__findKth(node.left, k)
        else:
            return self.__findKth(node.right, k-lcnt-1)

    def findKth(self, k):
        if self.root is None or k > self.root.size:
            return None
        else:
            return self.__findKth(self.root, k)

    def median(self):
        s = self.size()
        if s == 0:
            return 0
        result = 0
        if s % 2 == 1:
            result = self.findKth(s // 2 + 1)
        else:
            result = (self.findKth(s // 2) + self.findKth(s // 2 + 1)) / 2.0
        return result

    def printTree(self):
        if self.root is None:
            return ''
        else:
            return str(self.root)

def unitTest(n):
    random.seed(n)
    x = []
    t = Treap()
    for i in range(n):
        x.append(random.randint(0, n))
        t.insert(x[-1])
    for i in range(n):
        t.delete(x[i])
        t.insert(x[i]*x[i])
    x.sort()
    for i in range(n):
        assert t.findKth(i+1) == x[i]*x[i]

if __name__ == "__main__":
    unitTest(10)
    unitTest(100)

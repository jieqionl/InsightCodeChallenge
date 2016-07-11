# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 17:38:35 2016

@author: Jieqiong Liu
"""

import json
import time
import sys
import os

from graph import Graph, Vertex
from msg_queue import MsgQueue

class StreamEngine:
    def __init__(self, windowSize):
        self.graph = Graph()
        self.queue = MsgQueue()
        self.windowSize = windowSize
        
    def processPayment(self, payment):
        paytime = payment[2]
        
        # 1. dequeue old payments that are out of new window
        while not self.queue.isEmpty() and \
              self.queue.minTime() + self.windowSize < paytime:
            oldpayment = self.queue.peek()
            self.graph.delEdge(oldpayment[0], oldpayment[1])
            self.queue.dequeue()
        
        # 2. enqueue new payment
        if self.queue.isEmpty() or \
            paytime >= self.queue.maxTime() - self.windowSize:
            if not self.queue.isEmpty() and paytime < self.queue.maxTime():
                # time > window min time and < window max time -- out of order
                self.queue.insertRandomItem(payment)
            else:
                # time > window max time
                self.queue.enqueue(payment)
            self.graph.addEdge(payment[0], payment[1])
         
        # 3. return median degree
        return self.graph.findMedianDegree()
                
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Not enough arguments")
    else:
        print("Current directory"+os.getcwd())
        finname = sys.argv[1]
        fin = open(finname)
        foutname = sys.argv[2]
        fout = open(foutname, 'w')
        engine = StreamEngine(60)
        for line in fin:
            result = json.loads(line)
            actor = result['actor']
            target = result['target']
            tstr = result['created_time']
            t = time.mktime(time.strptime(tstr, '%Y-%m-%dT%H:%M:%SZ'))
            fout.write("%.2f\n"%((engine.processPayment((actor, target, t)))))
        fin.close()
        fout.close()

import heapq

class SlowMsgQueue():
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
        
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
        
    def insertRandomItem(self, item):
        for i in range(self.size()):
            if self.items[i][2] < item[2]:
                self.items.insert(i, item)
                return
        self.items.append(item)
    
    def size(self):
        return len(self.items)
        
    def peek(self):
        return self.items[-1]
        
    def minTime(self):
        return self.items[-1][2]
        
    def maxTime(self):
        return self.items[0][2]
        
    def show(self):
        print(self.items)
        
class PaymentMessage():
    def __init__(self, item):
        self.item = item
    
    def __lt__(self, other):
        return self.item[2] < other.item[2]
        
class MsgQueue():
    def __init__(self):
        self.heap = []
        self.maxT = 0.0
        
    def isEmpty(self):
        return self.heap == []
        
    def enqueue(self, item):
        heapq.heappush(self.heap, PaymentMessage(item))
        self.maxT = max(self.maxT, item[2])
        
    def insertRandomItem(self, item):
        self.enqueue(item)
        
    def dequeue(self):
        return heapq.heappop(self.heap).item
    
    def size(self):
        return len(self.heap)
        
    def peek(self):
        return self.heap[0].item
        
    def minTime(self):
        return self.heap[0].item[2]
        
    def maxTime(self):
        return self.maxT
        
    def show(self):
        print('[',end='')
        for item in self.heap:
            print(str(item.item)+',',end='')
        print(']')
        

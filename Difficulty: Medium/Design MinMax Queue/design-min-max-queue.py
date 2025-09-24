from collections import deque

class SpecialQueue:
    def __init__(self):
        
        self.mainQueue = deque()
        
        self.minDeque = deque()
       
        self.maxDeque = deque()

    def enqueue(self, x):
        
        self.mainQueue.append(x)

       
        while self.minDeque and self.minDeque[-1] > x:
            
            self.minDeque.pop()
        self.minDeque.append(x)

        
        while self.maxDeque and self.maxDeque[-1] < x:
            
            self.maxDeque.pop()
        self.maxDeque.append(x)

       

    def dequeue(self):
        if self.mainQueue:
            val = self.mainQueue.popleft()

           
            if self.minDeque and val == self.minDeque[0]:
                self.minDeque.popleft()

            
            if self.maxDeque and val == self.maxDeque[0]:
                self.maxDeque.popleft()

            

    def getFront(self):
               return self.mainQueue[0] if self.mainQueue else None

    def getMin(self):
        
        return self.minDeque[0] if self.minDeque else None

    def getMax(self):
        
        return self.maxDeque[0] if self.maxDeque else None
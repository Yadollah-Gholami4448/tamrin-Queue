class Queue:
    def __init__(self,max_size):
        self.max_size = max_size
        self.Q = [0] * max_size
        self.num = 0
        self.first = 0

    def enqueue(self, item):
        if self.num >= self.max_size :
            raise Exception(" Queue overflow")
        self.Q[(self.num + self.first)% self.max_size] = item
        self.num +=1

    def dequeue(self):
        if self.num == 0:
            raise Exception("Queue empty")
        item = self.Q[self.first]
        self.first = (self.first +1)% self.max_size
        self.num -=1
        return item
    def front(self):
        if self.num == 0:
            raise Exception("Queue empty")
        return self.Q[(self.first)]
    def is__empty(self):
        return self.num == 0
    def size(self):
        return self.num
    def is__full(self):
        return self.num >= self.max_size
    
    def delet_queue(self,x):
        if self.num == 0:
            raise Exception("queue empty")
        elif x > self.num :
            raise Exception("not find")
        item = self.Q[self.first]
        self.first = (self.first + x) % self.max_size
        self.num -=1        


q = Queue(10)
q.enqueue("rana")#[rana]
q.enqueue("vez")# [ rana, vez]
q.enqueue("arya")#[rana, vez, arya]
q.delet_queue(1)
print("queue size is : ",q.size())
print(q.dequeue(),"lefte the queue")
print("front of queue is :", q.front())
q.enqueue("milad")
q.dequeue()
q.dequeue()
q.dequeue()
print("it was a queue")
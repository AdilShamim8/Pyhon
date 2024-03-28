
class queue:
    def __init__(self):
        self.values=[]
    def enqueue(self,x):
        self.values.append(x)
    def dequeue (self):
        front=self.values[0]
        self.values=self.values[1:]
        return front
q1 = queue()
q1.enqueue(1)
q1.enqueue(10)
q1.enqueue(11)
q1.enqueue(100)
q1.enqueue(101)
q1.enqueue(110)
q1.enqueue(111)
q1.enqueue(1000)
q1.enqueue(1001)
q1.enqueue(1010)
print(q1.values)



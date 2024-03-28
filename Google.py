# class calculatuin:
#     def __init__(self,a,b):
#         print("Addition:", a + b)
#         print("Substraction:", a - b)
#         print("Multiplication:", a *b)
#         print("Divison:",a/b)
# cal = calculatuin(8,2)


# def sq_numbers(n):
#     for i in range(1,n+1):
#               yield i *i
# a = sq_numbers(3)
# print("The square of numbers 1,2,3 are:")
# print(next(a))
# print(next(a))
# print(next(a))







# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# # Creating nodes
# node1 = Node(9)
# node2 = Node(8)
# node3 = Node(7)
# node4 = Node(6)
# node5 = Node(5)

# # Linking nodes
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5



# # Printing the linked list
# current = node1
# while current is not None:
#     print(current.data, end="------>")
#     current = current.next
# print("None")









# class Node:
#     def __init__(self, data, next):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_beginning(self, data):
#         node = Node(data, self.head)
#         self.head = node

#     def print(self):
#         itr = self.head
#         llstr = ''
#         while itr:
#             suffix = '---->' if itr.next else ''
#             llstr += str(itr.data) + suffix
#             itr = itr.next
#         print(llstr)

# if __name__ == '__main__':
#     root = LinkedList()
#     root.insert_at_beginning(8)
#     root.insert_at_beginning(9)
#     root.print()























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






























# from collections import deque

# class Queue:
#     def __init__(self):
#         self.buffer = deque()

#     def enqueue(self, val):
#         self.buffer.appendleft(val)

#     def dequeue(self):
#         if len(self.buffer)==0:
#             print("Queue is empty")
#             return

#         return self.buffer.pop()

#     def is_empty(self):
#         return len(self.buffer) == 0

#     def size(self):
#         return len(self.buffer)

#     def front(self):
#         return self.buffer[-1]

# def produce_binary_numbers(n):
#     numbers_queue = Queue()
#     numbers_queue.enqueue("1")

#     for i in range(n):
#         front = numbers_queue.front()
#         print("   ", front)
#         numbers_queue.enqueue(front + "0")
#         numbers_queue.enqueue(front + "1")

#         numbers_queue.dequeue()


# if __name__ == '__main__':
#     produce_binary_numbers(10)




class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

def generate_binary_numbers(n):
    q = Queue()
    q.enqueue("1")

    for _ in range(n):
        binary_num = q.dequeue()
        print(binary_num)

        q.enqueue(binary_num + "0")
        q.enqueue(binary_num + "1")

# Print binary numbers from 1 to 10
generate_binary_numbers(10)

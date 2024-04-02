# based implementions of queue by linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def insert(self,item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def remove(self):
        if self.isEmpty():
            return
        # temp = self.front
        self.front = self.front.next
        
        if self.front == None:
            self.rear = None

    def display(self):
        if self.isEmpty():
            return
        while(self.front):
            print(self.front.data)
            self.front = self.front.next

instance = Queue()
instance.insert(5)
instance.insert(6)
instance.insert(7)
instance.insert(8)
# instance.display()
# instance.remove()
instance.display()
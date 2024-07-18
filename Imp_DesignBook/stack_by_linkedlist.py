class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack(Node):
    def __init__(self):
        # head is defualt none.
        self.head = None

    def isempty(self):
        if self.head is None:
            return True
        return False
    
    def push(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def pop(self):
        if self.isempty():
            return None
        else:
            poppendnode = self.head
            self.head = self.head.next
            poppendnode.next = None
            return poppendnode.data
    
    def peek(self):
        if self.isempty():
            return None
        return self.head.data
    
    def display(self):
        iternode = self.head
        
        if self.isempty():
            print("Stack underflow")
        
        else:
            while(iternode!=None):
                print(f' --> {iternode.data}')
                iternode = iternode.next
            return
        
stack = Stack()
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(7)
stack.push(1)
stack.display()
print("*" * 10)
stack.pop()
print("the top poped")
print("*" * 10)
stack.display()
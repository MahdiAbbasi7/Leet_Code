class Node:
    def __init__(self, data,) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList(Node):
    # Represent of head and tail in d-linked lists.
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def add(self, data):
        # create a new node.
        newNode = Node(data)
        # if list is empty.
        if self.head == None:
            # head and tail are points to the new Node
            self.head = self.tail = newNode
            # head's previous will point to None
            self.head.prev = None
            # tail's next will point to None,(last node of the list.)
            self.tail.next = None
        else:
            # newNode will be added after tail
            self.tail.next = newNode
            # newNode's previous will point to tail
            newNode.prev = self.tail
            # newNode will become new tail
            self.tail = newNode
            # As it is last node, tail's next will point to None
            self.tail.next = None
    
    def delete(self):
        # check whether list is empty
        if self.head == None :
            return
        else:
            # if list contain only one element
            if self.head != self.tail : 
                # head will point to next node in the list
                self.head = self.head.next
                # Previous node to current head will be made None
                self.head.prev = None
            else:
                self.head = self.tail = None
    
    def display(self):
        # Node current point to head
        curr = self.head
        if self.head == None :
            print('list is empty.')
            return
        while curr != None:
            print(curr.data)
            curr = curr.next
        print()

dll = DoublyLinkedList()
# add/delete from beginning
dll.add(1)
dll.add(2)
dll.add(3)
dll.add(4)
dll.display()



dll.delete()
dll.display()
dll.delete()
dll.delete()
dll.delete()
dll.display()
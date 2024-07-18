class Node :
    def __init__(self, data) -> None:
        self.data = data # Assign Data
        self.next = None # Initialize next node as null

# Linked list class contains a Node object
class LinkedList :
    def __init__(self) -> None:
        self.head = None

    # insert
    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # print
    def println(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # delete the first
    def delete(self, key):
        # Store head node
        temp = self.head
        # if head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key :
                self.head = temp.next
                temp = None
                return
        # search for the key to be deleted, keep track of the previous node as we need to change prev.next
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        # if the key was not present in linked list
            if temp == None:
                return
        # unlike the node from linked list
        prev.next = temp.next
        temp = None

sll = LinkedList()
sll.insert(7)
sll.insert(4)
sll.insert(3)
sll.println()
print("*" * 20)
sll.delete(7)
sll.println()



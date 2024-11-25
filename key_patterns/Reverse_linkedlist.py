class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def reverse_list(head):
    prev = None
    current = head
    while current:
        # Store next
        next_node = current.next

        # Reverse current node's next pointer
        current.next = prev

        # Move pointers one position ahead
        prev = current
        current = next_node

    # Return the head of reversed linked list
    return prev


def print_list(node):
    while node is not None:
        print(f" {node.val}", end="")
        node = node.next
    print()


if __name__ == "__main__":
    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Given Linked list:", end="")
    print_list(head)

    head = reverse_list(head)

    print("Reversed Linked List:", end="")
    print_list(head)

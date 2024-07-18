class Node:
    def __init__(self, info, priority) -> None:
        self.data = info
        self.priority = priority

class PriorityQueue(Node):
    def __init__(self):
        self.queue = []
    
    def insert(self,node):
        if self.size() == 0:
            self.queue.append(node)
        else:
            for x in range(0, self.size()):
                if node.priority >= self.queue[x].priority:
                    # if we have traversed the complete queue
                    if x == (self.size()-1):
                        # add new node to the end of the queue
                        self.queue.insert(x+1, node)
                    else:
                        continue
                else:
                    self.queue.insert(x, node)
                    return True
    
    def delete(self):
        return self.queue.pop(0)
    
    def show(self):
        for x in self.queue:
            print(f'{str(x.data)} - {str(x.priority)}')

    def size(self):
        return len(self.queue)
    

pq = PriorityQueue()
node1 = Node(12, 5)
node2 = Node(45, 3)
node3 = Node(23, 10)
node4 = Node(4, 4)
node5 = Node(33, 2)
pq.insert(node1)
pq.insert(node2)
pq.insert(node3)
pq.insert(node4)
pq.insert(node5)

pq.show()
print('#' * 20)
pq.delete()
print('#' * 20)
pq.show()
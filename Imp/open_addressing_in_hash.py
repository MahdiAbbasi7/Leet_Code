# Program to implement hashing with linear probing

class hashTable:
    def __init__(self) -> None:
        self.size = int(input('Please enter the size of the hash table : '))
        # initialize table with all elements 0
        self.table = list(0 for i in range(self.size))
        self.elementCount = 0
        self.comparisons = 0
        

    def isFull(self):
        '''method that checks if the hash table is full or not'''
        if self.elementCount == self.size:
            return True
        return False # todo: add else
    
    def hashFunction(self, element):
        '''method that returns position for a given element'''
        # k mode size
        return element % self.size

    def insert(self, element):
        '''method that inserts elements inside tha hash table'''
        # check if table is full
        if self.isFull():
            print('Hash Table Full.')
            return False
        
        isSorted = False
        position = self.hashFunction(element)

        # checking if the position is empty
        if self.table[position] == 0:
            self.table[position] = element
            print(f'Element {str(element)} at position {str(position)}')
            isSorted = True
            self.elementCount += 1
        # collision occurred hence we do linear probing
        else:
            print("Collision has occurred for element " + 
                  str(element) + " at position " + 
                  str(position) + " finding new position.")
            while self.table[position] != 0:
                position +=1
                if position >= self.size:
                    position = 0
                self.table[position] = element
                isStored = True # todo add self
                self.elementCount += 1
            return isSorted

    def search(self, element):
        '''method that searches for an element in the table
        and returns its position if found else return False'''
        found = False
        position = self.hashFunction(element)
        self.comparisons += 1
        
        if (self.table[position] == element) : 
            return position
            isFound = True
        
        # if element is not found at position returned hash function
        # then first we search element from position+1 to end
        # if not found then we search element from position-1 to 0
        else: 
            temp = position - 1
            # check if the element is sorted between position+1 to size
            while position < self.size:
                if self.table[position] != element:
                    position += 1
                    self.comparisons += 1
                else:
                    return position
            
            # now checking if the element is sorted between position-1 to 0
            position = temp
            while position >= 0 : 
                if self.table[position] != element:
                    position -= 1
                    self.comparisons += 1
                else:
                    return position
            if not found:
                print('Element not found')
                return False

    def remove(self, element):
        '''method to remove an element from the table'''
        position = self.table[element]
        if position:
            self.table[position] = 0
            print("Element " + str(element) + " is deleted")
            self.elementCount -= 1
        else:
            print("Element is not present in the hash table")
            return

    def display(self):
        '''method to display the hash table'''
        print("\n")
        for i in range(self.size):
            print(str(i) + " = " + str(self.table[i]))
            print("The number of elements in the table are : " +
            str(self.elementCount))
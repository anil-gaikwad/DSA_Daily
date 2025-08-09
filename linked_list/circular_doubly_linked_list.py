class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        current_node = self.head
        result = ""
        
        while current_node:
            result += str(current_node.value)
            current_node = current_node.next
            if current_node == self.head: break
            result += " <-> "
        
        return result

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length +=1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head = new_node

        self.length +=1

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break
    
    def reverse_traverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev
            if current_node == self.tail:
                break

    
    def search(self, target):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == target:
                return True, index
            current_node = current_node.next
            if current_node == self.head:
                break
            index +=1
        return False, index
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index > self.length //2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length -1 , index, -1):
                current_node = current_node.prev
        return current_node


    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return "Index Out bounds"

        if index ==0:
            self.prepend(value)
            return 
        elif index == self.length:
            self.append(value)
            return
        
        new_node = Node(value)
        temp_node = self.get(index-1)
        
        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length +=1

    
    def pop_first(self):
        if not self.head:
            return None
        
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
            popped_node.prev = None
            self.head.prev = self.tail
            self.tail.next = self.head

        self.length -=1
        return popped_node

    def pop(self):
        if not self.tail:
            return None
        
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            popped_node.next = None
            popped_node.prev = None
            self.tail.next = self.head
            self.head.prev = self.tail

        self.length -=1
        return popped_node
    

    def remove(self, index):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        
        popped_node = self.get(index)
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        
        popped_node.next = None
        popped_node.prev = None
        self.length -=1
        return popped_node


cdl = CircularDoublyLinkedList()
cdl.append(1)
cdl.append(2)
cdl.append(3)
cdl.append(4)
print(cdl)
print(cdl)
cdl.remove(3)
print(cdl)






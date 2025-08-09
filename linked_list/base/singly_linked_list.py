

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''

        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        return result


    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
    
    def insert(self, index, value):
        new_node = Node(value)
        temp_node = self.head

        if index < 0 or index > self.length:
            return False
        elif index ==0:
            self.head = new_node
            self.tail = new_node
        else:
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length +=1


    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def search(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True 
            current = current.next
        return False
    
    def get(self, index):
        if index == -1:
            return self.tail
        if index < 0 or index >= self.length:
            return None

        current = self.head

        for _ in range(index):
            current = current.next
        return current
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def poped_first(self):
        if self.length == 0:
            return None
        poped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            poped_node.next = None
       
        self.length -=1
        return poped_node


    def pop(self):
        if self.length == 0:
            return None
        
        poped_node = self.tail
        if self.length ==1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next  
            self.tail = temp
            temp.next = None 
        self.length -= 1
        return poped_node
        
    def remove(self, index):
        if index >= self.length or index < 0:
            return None
        if self.length == 0:
            return self.poped_first()
        if self.length == -1:
            return self.pop()
        
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -=1
        return popped_node


    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0




linked_list = LinkedList()
linked_list.insert(-1,9)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
print(linked_list)
# linked_list.prepend(5)
linked_list.insert(2, 6)
print(linked_list)
# print(linked_list.traverse())
print(linked_list.search(12))
# print(linked_list.get(-1))
print(linked_list.set_value(2, 9))
print(linked_list)
# print(linked_list.poped_first())
# print(linked_list)
# print(linked_list.pop())
# print(linked_list)
print(linked_list.remove(1))
print(linked_list)
print(linked_list.delete_all())
print(linked_list)

        

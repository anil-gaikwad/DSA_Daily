
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = next

    
class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curnode = self.head
        while curnode:
            yield curnode
            curnode = curnode.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
    
    def push(self, value):
        node = Node(value)
        node.next =self.LinkedList.head
        self.LinkedList.head = node
        
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            node_value = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return node_value

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            node_value = self.LinkedList.head.value
            return node_value

    def delete(self):
        self.LinkedList.head = None

customStack = Stack()
print(customStack.isEmpty())
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack)
print("")
customStack.pop()
print(customStack)
print(customStack.peek())


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None  # Pointer to the next node


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]  # O(n) - Traverse all nodes
        return '\n'.join(values)
    
    def isEmpty(self):
        return self.LinkedList.head is None  # O(1)

    def push(self, value):
        node = Node(value)                   # O(1)
        node.next = self.LinkedList.head     # O(1)
        self.LinkedList.head = node          # O(1)
        
    def pop(self):
        if self.isEmpty():                   # O(1)
            return "Stack is empty"
        node_value = self.LinkedList.head.value  # O(1)
        self.LinkedList.head = self.LinkedList.head.next  # O(1)
        return node_value

    def peek(self):
        if self.isEmpty():                   # O(1)
            return "Stack is empty"
        return self.LinkedList.head.value    # O(1)

    def delete(self):
        self.LinkedList.head = None          # O(1)


# ------------------ Sample Usage ------------------
customStack = Stack()
print(customStack.isEmpty())  # O(1)
customStack.push(2)           # O(1)
customStack.push(3)           # O(1)
customStack.push(4)           # O(1)

print(customStack)            # O(n)

print("")
customStack.pop()             # O(1)
print(customStack)            # O(n)
print(customStack.peek())     # O(1)

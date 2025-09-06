class Node:
    """A single node in a doubly linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class DoublyLinkedList:
    """Doubly Linked List implementation."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        """Return a string representation of the list. O(n)"""
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += ' <-> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        """Add a node at the end. O(1)"""
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        """Add a node at the beginning. O(1)"""
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def traverse(self):
        """Print all values from head to tail. O(n)"""
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def reverse_traverse(self):
        """Print all values from tail to head. O(n)"""
        current = self.tail
        while current:
            print(current.value)
            current = current.prev

    def search(self, target):
        """Return (True, index) if value exists, else (False, length). O(n)"""
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return True, index
            current = current.next
            index += 1
        return False, index

    def get(self, index):
        """Get node at specific index. O(n)"""
        if index < 0 or index >= self.length:
            return None
        if index <= self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev
        return current

    def set_value(self, index, value):
        """Update value of node at index. O(n)"""
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        """Insert a node at a specific index. O(n)"""
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        prev_node = self.get(index - 1)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next.prev = new_node
        prev_node.next = new_node
        self.length += 1
        return True

    def pop_first(self):
        """Remove first node. O(1)"""
        if not self.head:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop(self):
        """Remove last node. O(1)"""
        if not self.tail:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        """Remove node at specific index. O(n)"""
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        popped_node = self.get(index)
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        popped_node.next = popped_node.prev = None
        self.length -= 1
        return popped_node


# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.append(40)
    print("Initial List:", dll)
    print("Removed:", dll.remove(2))
    print("List After Remove:", dll)
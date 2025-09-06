class Node:
    """A single node in a circular doubly linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class CircularDoublyLinkedList:
    """Circular Doubly Linked List implementation."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        """Return a string representation of the list. O(n)"""
        if not self.head:
            return ""
        result = ""
        current = self.head
        while True:
            result += str(current.value)
            current = current.next
            if current == self.head:
                break
            result += " <-> "
        return result

    def append(self, value):
        """Add a node at the end. O(1)"""
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        """Add a node at the beginning. O(1)"""
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def traverse(self):
        """Traverse list forward and print values. O(n)"""
        if self.length == 0:
            return
        current = self.head
        while True:
            print(current.value)
            current = current.next
            if current == self.head:
                break

    def reverse_traverse(self):
        """Traverse list backward and print values. O(n)"""
        if self.length == 0:
            return
        current = self.tail
        while True:
            print(current.value)
            current = current.prev
            if current == self.tail:
                break

    def search(self, target):
        """Return (True, index) if found, else (False, -1). O(n)"""
        if self.length == 0:
            return False, -1
        index = 0
        current = self.head
        while True:
            if current.value == target:
                return True, index
            current = current.next
            index += 1
            if current == self.head:
                break
        return False, -1

    def get(self, index):
        """Get node at specific index. O(n)"""
        if index < 0 or index >= self.length:
            return None
        # Choose shortest direction
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
        """Insert node at specific index. O(n)"""
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")
        if index == 0:
            self.prepend(value)
            return
        if index == self.length:
            self.append(value)
            return
        new_node = Node(value)
        prev_node = self.get(index - 1)
        next_node = prev_node.next
        new_node.prev = prev_node
        new_node.next = next_node
        prev_node.next = new_node
        next_node.prev = new_node
        self.length += 1

    def pop_first(self):
        """Remove and return first node. O(1)"""
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            popped_node.next = popped_node.prev = None
        self.length -= 1
        return popped_node

    def pop(self):
        """Remove and return last node. O(1)"""
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            popped_node.next = popped_node.prev = None
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
        node_to_remove = self.get(index)
        node_to_remove.prev.next = node_to_remove.next
        node_to_remove.next.prev = node_to_remove.prev
        node_to_remove.next = node_to_remove.prev = None
        self.length -= 1
        return node_to_remove


# Example usage
if __name__ == "__main__":
    cdl = CircularDoublyLinkedList()
    cdl.append(1)
    cdl.append(2)
    cdl.append(3)
    cdl.append(4)
    print("Initial:", cdl)
    cdl.remove(3)
    print("After remove:", cdl)

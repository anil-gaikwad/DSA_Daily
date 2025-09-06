class Node:
    """A single node in a circular singly linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class CSLinkedList:
    """Circular Singly Linked List implementation."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        """Return a string representation of the list. O(n)"""
        if not self.head:
            return ""
        result = ""
        temp_node = self.head
        while True:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += " -> "
        return result

    def append(self, value):
        """Add a node at the end. O(1)"""
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        """Add a node at the beginning. O(1)"""
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def insert(self, index, value):
        """Insert a node at a specific index. O(n)"""
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        prev_node = self.get(index - 1)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.length += 1

    def traverse(self):
        """Print all values in the list. O(n)"""
        if self.length == 0:
            return
        current = self.head
        while True:
            print(current.value)
            current = current.next
            if current == self.head:
                break

    def search(self, target):
        """Return True if value exists, else False. O(n)"""
        if self.length == 0:
            return False
        current = self.head
        while True:
            if current.value == target:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def get(self, index):
        """Get node at specific index. O(n)"""
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set_value(self, index, value):
        """Update value of node at index. O(n)"""
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def pop_first(self):
        """Remove and return first node. O(1)"""
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop(self):
        """Remove and return last node. O(n)"""
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            prev = self.head
            while prev.next != self.tail:
                prev = prev.next
            prev.next = self.head
            self.tail = prev
            popped_node.next = None
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
        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node


# Example usage
if __name__ == "__main__":
    csll = CSLinkedList()
    csll.insert(0, 1)
    csll.insert(1, 2)
    csll.insert(2, 3)
    print("Initial List:", csll)
    csll.set_value(1, 4)
    print("After set_value:", csll)
    csll.remove(1)
    print("After remove:", csll)

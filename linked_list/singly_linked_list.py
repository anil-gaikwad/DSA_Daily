class Node:
    """A single node in a singly linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    """Singly Linked List implementation."""

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
                result += ' -> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        """Add a node at the end. O(1)"""
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        """Add a node at the beginning. O(1)"""
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

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
        prev_node.next = new_node
        self.length += 1
        return True

    def traverse(self):
        """Print all values in the list. O(n)"""
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def search(self, target):
        """Return True if value exists, else False. O(n)"""
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
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
        """Remove first node. O(1)"""
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop(self):
        """Remove last node. O(n)"""
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            prev_node = self.get(self.length - 2)
            prev_node.next = None
            self.tail = prev_node
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

    def delete_all(self):
        """Delete entire list. O(1)"""
        self.head = None
        self.tail = None
        self.length = 0
        return "List deleted."


# ---------------- Example usage ----------------
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(2)
    ll.append(3)
    ll.append(4)
    print("Initial List:", ll)

    ll.prepend(1)
    print("After Prepend:", ll)

    ll.insert(2, 6)
    print("After Insert:", ll)

    print("Search 3:", ll.search(3))
    print("Set index 2 to 9:", ll.set_value(2, 9))
    print("Updated List:", ll)

    print("Removed:", ll.remove(1))
    print("List After Remove:", ll)

    ll.delete_all()
    print("After Delete All:", ll)

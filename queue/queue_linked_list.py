class Node:
    """Node for a singly linked list."""
    def __init__(self, value=None):
        self.value = value  # O(1)
        self.next = None    # O(1)

    def __str__(self):
        return str(self.value)


class LinkedList:
    """Singly linked list structure."""
    def __init__(self):
        self.head = None  # O(1)
        self.tail = None  # O(1)

    def __iter__(self):
        """Iterate through the linked list. O(n)"""
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


class Queue:
    """Queue (FIFO) implementation using linked list."""
    def __init__(self):
        self.linkedlist = LinkedList()  # O(1)

    def __str__(self):
        values = [str(node.value) for node in self.linkedlist]  # O(n)
        return "Front -> " + " -> ".join(values) + " -> Rear" if values else "Queue is empty"

    def is_empty(self):
        return self.linkedlist.head is None  # O(1)

    def enqueue(self, value):
        new_node = Node(value)  # O(1)
        if self.is_empty():     # O(1)
            self.linkedlist.head = new_node  # O(1)
            self.linkedlist.tail = new_node  # O(1)
        else:
            self.linkedlist.tail.next = new_node  # O(1)
            self.linkedlist.tail = new_node       # O(1)

    def dequeue(self):
        if self.is_empty():  # O(1)
            return "Error: Queue is empty."
        removed_node = self.linkedlist.head  # O(1)
        if self.linkedlist.head == self.linkedlist.tail:  # O(1)
            self.linkedlist.head = None  # O(1)
            self.linkedlist.tail = None  # O(1)
        else:
            self.linkedlist.head = self.linkedlist.head.next  # O(1)
        return removed_node.value  # O(1)

    def peek(self):
        if self.is_empty():  # O(1)
            return "Error: Queue is empty."
        return self.linkedlist.head.value  # O(1)

    def delete(self):
        self.linkedlist.head = None  # O(1)
        self.linkedlist.tail = None  # O(1)


# ------------------ Example usage ------------------
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)  # O(1)
    queue.enqueue(2)  # O(1)
    queue.enqueue(3)  # O(1)

    print("Current Queue:")
    print(queue)  # O(n)

    print("\nFront Element:", queue.peek())  # O(1)

    print("\nDequeued:", queue.dequeue())  # O(1)
    print("After Dequeue:")
    print(queue)  # O(n)

    queue.delete()  # O(1)
    print("\nAfter Delete:")
    print(queue)

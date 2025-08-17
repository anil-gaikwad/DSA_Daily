class Queue:
    """Simple Queue (FIFO) implementation using Python list."""

    def __init__(self):
        self.items = []  # O(1)

    def __str__(self):
        return " ".join(str(x) for x in self.items)  # O(n)

    def is_empty(self):
        return len(self.items) == 0  # O(1)

    def enqueue(self, value):
        self.items.append(value)  # O(1) amortized
        return f"Element '{value}' inserted."

    def dequeue(self):
        if self.is_empty():  # O(1)
            return "Error: Queue is empty."
        return self.items.pop(0)  # O(n) - List shifting cost

    def peek(self):
        if self.is_empty():  # O(1)
            return "Error: Queue is empty."
        return self.items[0]  # O(1)

    def delete(self):
        self.items = []  # O(1)


# ------------------ Example usage ------------------
if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(2)  # O(1)
    queue.enqueue(3)  # O(1)
    queue.enqueue(4)  # O(1)

    print("Current Queue:")
    print(queue)  # O(n)

    queue.dequeue()  # O(n)
    print("\nAfter Dequeue:")
    print(queue)  # O(n)

    print("\nFront Element:", queue.peek())  # O(1)

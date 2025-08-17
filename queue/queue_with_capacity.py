class CircularQueue:
    """Circular Queue (FIFO) implementation using a fixed-size list."""

    def __init__(self, max_size):
        self.items = [None] * max_size  # O(1)
        self.max_size = max_size        # O(1)
        self.start = -1                 # O(1)
        self.top = -1                   # O(1)

    def __str__(self):
        return " ".join(str(x) if x is not None else "None" for x in self.items)  # O(n)

    def is_full(self):
        return ((self.top + 1) % self.max_size) == self.start  # O(1)

    def is_empty(self):
        return self.start == -1  # O(1)

    def enqueue(self, value):
        if self.is_full():  # O(1)
            return "Error: Queue is full."
        if self.is_empty():  # O(1)
            self.start = 0
            self.top = 0
        else:
            self.top = (self.top + 1) % self.max_size  # O(1)
        self.items[self.top] = value  # O(1)
        return f"Element '{value}' inserted."

    def dequeue(self):
        if self.is_empty():  # O(1)
            return "Error: Queue is empty."
        removed_value = self.items[self.start]  # O(1)
        self.items[self.start] = None  # O(1)
        if self.start == self.top:  # O(1)
            self.start = -1  # O(1)
            self.top = -1    # O(1)
        else:
            self.start = (self.start + 1) % self.max_size  # O(1)
        return removed_value

    def peek(self):
        if self.is_empty():  # O(1)
            return "Error: Queue is empty."
        return self.items[self.start]  # O(1)

    def delete(self):
        self.items = [None] * self.max_size  # O(n)
        self.start = -1  # O(1)
        self.top = -1    # O(1)
        return "Queue deleted."


# ------------------ Example usage ------------------
if __name__ == "__main__":
    cq = CircularQueue(3)
    print(cq.enqueue(2))  # O(1)
    print(cq.enqueue(3))  # O(1)
    print(cq.enqueue(4))  # O(1) - Queue is now full

    print("\nCurrent Queue:")
    print(cq)  # O(n)

    print("\nDequeued:", cq.dequeue())  # O(1)
    print("After Dequeue:")
    print(cq)  # O(n)

    print("\nFront Element:", cq.peek())  # O(1)

    print("\n" + cq.delete())  # O(n)
    print("After Delete:")
    print(cq)  # O(n)

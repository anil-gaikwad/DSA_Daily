class Stack:
    """Simple Stack (LIFO) implementation using Python list."""

    def __init__(self):
        """Initialize an empty stack. O(1)"""
        self.items = []  # O(1)

    def __str__(self):
        """Return stack elements from top to bottom. O(n)"""
        return "\n".join(str(item) for item in self.items)  # O(n)

    def is_empty(self):
        """Check if stack is empty. O(1)"""
        return len(self.items) == 0  # O(1)

    def push(self, value):
        """Push an element onto the stack. O(1) amortized"""
        self.items.append(value)  # O(1) amortized
        return f"Element '{value}' inserted."

    def pop(self):
        """Remove and return the top element. O(1)"""
        if self.is_empty():  # O(1)
            return "Error: Stack is empty."
        return self.items.pop()  # O(1)

    def peek(self):
        """Return the top element without removing it. O(1)"""
        if self.is_empty():  # O(1)
            return "Error: Stack is empty."
        return self.items[-1]  # O(1)


# ------------------ Example usage ------------------
if __name__ == "__main__":
    stack = Stack()
    print(stack.push(2))  # O(1)
    print(stack.push(3))  # O(1)

    print("\nCurrent Stack:")
    print(stack)  # O(n)

    print("\nTop Element:", stack.peek())  # O(1)
    print("Popped Element:", stack.pop())  # O(1)
    print("After Pop:")
    print(stack)  # O(n)

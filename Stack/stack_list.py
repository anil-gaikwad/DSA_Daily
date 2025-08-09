class Stack:
    """Simple Stack (LIFO) implementation."""

    def __init__(self):
        self.tems = []  # O(1) - Creating an empty list

    def __str__(self):
        return "\n".join(str(item) for item in self.tems)  # O(n) - Iterates through all elements

    def is_empty(self):
        return len(self.tems) == 0  # O(1) - Length check

    def push(self, value):
        self.tems.append(value)  # O(1) amortized - Append at end of list
        return f"Element '{value}' inserted."

    def pop(self):
        if self.is_empty():
            return "Error: Stack is empty."
        return self.tems.pop()  # O(1) - Remove from end of list

    def peek(self):
        if self.is_empty():
            return "Error: Stack is empty."
        return self.tems[-1]  # O(1) - Access last element


# Example usage
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

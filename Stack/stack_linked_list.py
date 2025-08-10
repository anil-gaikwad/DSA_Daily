class Node:
    """Represents a node in a singly linked list."""
    def __init__(self, value=None):
        self.value = value  # O(1)
        self.next = None    # O(1) - Pointer to the next node


class LinkedList:
    """Singly linked list used as the base for the stack."""
    def __init__(self):
        self.head = None  # O(1)

    def __iter__(self):
        """Iterates over all nodes in the linked list. O(n)"""
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


class Stack:
    """Stack implementation using a singly linked list (LIFO)."""
    def __init__(self):
        self.linked_list = LinkedList()  # O(1)

    def __str__(self):
        """Returns a string representation of the stack from top to bottom. O(n)"""
        values = [str(node.value) for node in self.linked_list]  # O(n)
        return "\n".join(values)

    def is_empty(self):
        """Checks if the stack is empty. O(1)"""
        return self.linked_list.head is None

    def push(self, value):
        """Pushes an element onto the stack. O(1)"""
        new_node = Node(value)                  # O(1)
        new_node.next = self.linked_list.head   # O(1)
        self.linked_list.head = new_node        # O(1)

    def pop(self):
        """Removes and returns the top element of the stack. O(1)"""
        if self.is_empty():                     # O(1)
            return "Stack is empty"
        top_value = self.linked_list.head.value # O(1)
        self.linked_list.head = self.linked_list.head.next  # O(1)
        return top_value

    def peek(self):
        """Returns the top element without removing it. O(1)"""
        if self.is_empty():                     # O(1)
            return "Stack is empty"
        return self.linked_list.head.value      # O(1)

    def delete(self):
        """Deletes the entire stack. O(1)"""
        self.linked_list.head = None


# ------------------ Example Usage ------------------
if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())  # O(1)
    
    stack.push(2)            # O(1)
    stack.push(3)            # O(1)
    stack.push(4)            # O(1)

    print("\nCurrent Stack:")
    print(stack)             # O(n)

    stack.pop()              # O(1)
    print("\nAfter Pop:")
    print(stack)             # O(n)

    print("\nTop Element:", stack.peek())  # O(1)

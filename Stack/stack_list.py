class Stack:
    def __init__(self):
        self.list = []
    

    def __str__(self):
        values = [str(x) for x in self.list]
        return "\n".join(values)

    def isEmpty(self):
        if not self.list:
            return True
        return False

    def push(self, value):
        self.list.append(value)
        return "Element Inserted"
    

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list.pop()


    def peek(self):
        if self.isEmpty():
            return " Stack is empty"
        else:
            return self.list[len(self.list) -1]


st = Stack()
st.push(2)
st.push(3)

print(st)
print(st.peek())
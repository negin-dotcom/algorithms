class Stack:
    def __init__(self, max_size: int):
        if max_size < 0:
            raise ValueError("max_size must be positive")
        
        self.s = [None] * max_size 
        self.top = -1

    def size(self):
        return len(self.s)

    def push(self, new_data):
        if self.is_full():
            raise OverflowError("Stack is full")

        self.top += 1
        self.s[self.top] = new_data 

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        popped_item = self.s[self.top]
        self.s[self.top] = None
        self.top -= 1

        return popped_item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        return self.s[self.top]

    def size(self):
        return self.top + 1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.s) - 1

    def __str__(self):
        items = [str(item) for item in self.s if item is not None]
        return "[" + ", ".join(items) + "]"

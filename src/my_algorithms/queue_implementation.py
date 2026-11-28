class Queue:
    """Queue is implemented as a circular buffer."""
    
    def __init__(self, max_size):
        if max_size < 0:
            raise ValueError("max_size must be positive")

        self.q = [None] * max_size
        self.first = 0
        self.last = 0
        self.count = 0

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == len(self.q)

    def enqueue(self, new_item):
        if self.is_full():
            raise OverflowError("Queue is full")

        self.q[self.last] = new_item
        self.last = (self.last + 1) % len(self.q)
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        dequeued_item = self.q[self.first]
        self.q[self.first] = None 
        self.first = (self.first + 1) % len(self.q)
        self.count -= 1

        return dequeued_item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.q[self.first]

    def __str__(self):
        items = [str(item) for item in self.q if item is not None]
        return "[" + ", ".join(items) + "]"

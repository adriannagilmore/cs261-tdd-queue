# Queue: A queue.
# Your implementation should pass the tests in test_queue.py.
# Adrianna Gilmore

# Hint: pip3 install llist
from llist import sllist

class Queue:

    def __init__(self):
        self.data = sllist()
        self.length = 0

    def enqueue(self, value):
        self.data.append(value)
        self.length += 1

    def dequeue(self):
        self.length -= 1
        return self.data.popleft()
    
    def is_empty(self):
        return self.length == 0


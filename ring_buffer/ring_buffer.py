class RingBuffer:
    def __init__(self, capacity):
        from collections import deque
        self.capacity = capacity
        self.filled = []
        self.data = deque(maxlen=capacity)

    def append(self, item):
        self.data.append(item)
        if self.data.index == 4:
            self.data.appendleft(item)

    def get(self):
        for i in self.data:
            self.filled.append(i)
        return self.filled
class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def full(self):
        return len(self.items) == self.limit

    def push(self, item):
        if not self.full():
            self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def search(self, target):
        length = self.size() - 1
        for i in range(len(self.items)):
            if target == self.items[i]:
                return length
            elif target != self.items[i]:
                length -= 1
        return -1   
class Stack:

    def __init__(self, capacity:int = 5):
        self.S = [None] * capacity
        self.ptr = 0
        self.capacity = capacity

    def isEmpty(self):
        return self.ptr <= 0

    def len(self):
        return self.ptr

    def isFull(self):
        return self.ptr >= self.capacity

    def push(self, item):
        if self.isFull():
            print("overflow")
        else:
            self.S[self.ptr] = item
            self.ptr += 1

    def pop(self):
        if self.isEmpty():
            print("underflow")
        else:
            self.ptr -= 1
            return self.S[self.ptr]

    def peek(self):
        if self.isEmpty():
            print("underflow")
        else: return self.S[self.ptr -1]

## Test

s = Stack()

print(s.isEmpty())
print(s.isFull())
s.push(1)
print(s.peek())
s.push(2)
print(s.peek())
s.push(3)
print(s.peek())
s.push(4)
print(s.peek())
s.push(5)
print(s.peek())
s.push(6)
print(s.isFull())
print(s.peek())
s.pop()
print(s.peek())
s.pop()
print(s.peek())
s.pop()
print(s.peek())
s.pop()
print(s.peek())
s.pop()
print(s.peek())
print(s.isEmpty())
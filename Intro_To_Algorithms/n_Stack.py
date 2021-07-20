class Stack:

    def __init__(self):
        self.S = []
        self.ptr = 0
        # self.capacity

    def isEmpty(self):
        return self.ptr <= 0

    def __len__(self):
        return self.ptr

    def push(self, item):
        self.S.append(item)
        self.ptr += 1

    def pop(self):
        if self.isEmpty():
            print("underflow")
        self.ptr -= 1
        return self.S[self.ptr]

    def peek(self):
        if self.isEmpty():
            print("underflow")
        return self.S[self.ptr - 1]

##테스트

stk = Stack()

print(stk.isEmpty())
stk.push(1)
print(stk.isEmpty())
stk.push(2)
print(stk.peek())
stk.push(4)
print(stk.peek())
print(stk.pop())
print(stk.peek())
print("***")
print(stk.__len__())
print(stk.isEmpty())
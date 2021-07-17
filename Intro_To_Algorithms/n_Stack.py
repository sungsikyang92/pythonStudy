# Stack, LIFO
# 후입선출 - 나중에 들어온 것이 먼저 나온다
# 1.  STACK CLASS 생성
# 2. STACK을 저장할 LIST 생성
# 3. STACK이 비어있는지 확인 isEmpty
# 4. STACK PUSH(차곡차곡 쌓임으로 append 사용)
# 5. STACK의 길이 확인 len
# 6. STACK POP(LIST의 마지막 인덱스 -1 추출)
# 7. STACK의 가장 최근에 넣은 원소 확인

class Stack:

    def __init__(self):
        self.S = []

    def isEmpty(self):
        return len(self.S) == 0

    def push(self, item):
        self.S.append(item)

    def __len__(self):
        return len(self.S)

    def pop(self):
        if not self.isEmpty():
            return self.S.pop(-1)
        else:
            print("underflow")

    def peek(self):
        if not self.isEmpty():
            return self.S[-1]
        else:
            print("underflow")
Stack = Stack()
print(Stack)
print(Stack.isEmpty())
Stack.push(1)
print(len(Stack))
Stack.push(2)
print(Stack.peek())
Stack.push(3)
print(Stack.peek())
Stack.pop()
print(Stack.peek())
Stack.push(4)
Stack.push(6)
Stack.push(5)
print(Stack.__len__())
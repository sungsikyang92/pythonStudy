import sys
from collections import deque

deque = deque()
inp = int(input())

def push_front(queue, x):
    queue.appendleft(x)

def push_back(queue, x):
    queue.append(x)

def pop_front(deque):
    return deque.popleft() if deque else -1

def pop_back(deque):
    return deque.pop() if deque else -1

def size(queue):
    return len(deque)

def empty(queue):
    return 1 if not queue else 0

def front(queue):
    return queue[0] if queue else -1

def back(queue):
    return queue[-1] if queue else -1

for _ in range(inp):
    cmd = sys.stdin.readline().split()
    order = cmd[0]

    if order == "push_front":
        push_front(deque, cmd[1])

    elif order == "push_back":
        push_back(deque, cmd[1])

    elif order == "pop_front":
        print(pop_front(deque))

    elif order == "pop_back":
        print(pop_back(deque))

    elif order == "size":
        print(size(deque))

    elif order == "empty":
        print(empty(deque))

    elif order == "front":
        print(front(deque))

    elif order == "back":
        print(back(deque))
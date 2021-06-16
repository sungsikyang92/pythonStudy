import sys
from collections import deque


def push(queue, x):
    queue.append(x)


def pop(deque):
    return deque.popleft() if deque else -1


def size(queue):
    return len(queue)


def empty(queue):
    return 1 if not queue else 0


def front(queue):
    return queue[0] if queue else -1


def back(queue):
    return queue[-1] if queue else -1


deque = deque()

inp = int(input())

for _ in range(inp):
    cmd = sys.stdin.readline().rstrip().split()
    order = cmd[0]

    if (order == "push"):
        push(deque, cmd[1])
    elif (order == "pop"):
        print(pop(deque))
    elif (order == "size"):
        print(size(deque))
    elif (order == "empty"):
        print(empty(deque))
    elif (order == "front"):
        print(front(deque))
    elif (order == "back"):
        print(back(deque))

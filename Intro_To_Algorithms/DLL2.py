class Node:
    def __init__(self, data, prev = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next

class DLL:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.size = 0

    def listsize(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    # 노드 선택
    def selectNode(self, idx):
        # idx가 리스트보다 클때
        if idx > self.size:
            print("overflow")
            return None
        # idx가 0일때는, head이다.
        elif idx == 0:
            return self.head
        # idx가 리스트의 사이즈와 같을때는 맨 끝으로 tail이다.
        elif idx == self.size:
            return self.tail
        # idx가 리스트의 절반보다 작거나 같을경우로 반을 나누어 검색의 속도를 빠르게 해준다.
        elif idx <= self.size//2:
            target = self.head
            for _ in range(idx):
                target = target.next
            return target
        else:
            target = self.tail
            for _ in range(self.size - idx):
                target = target.prev
            return target

    # 왼쪽삽입
    def appendleft(self, data):
        if self.is_empty():
            self.head = Node(data)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.head
            self.head = Node(data, None, self.head)
            tmp.prev = self.head
        self.size += 1

    # 삽입
    def append(self, data):
        if self.is_empty():
            self.head = Node(data)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.tail.prev
            newNode = Node(data, tmp, self.tail)
            tmp.next = newNode
            self.tail.prev = newNode
        self.size += 1

    #원하는 위치에 insert
    def insert(self, data, idx):
        if self.is_empty():
            self.head = Node(data)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.selectNode(idx)
            if tmp == None:
                return
            if tmp == self.head:
                self.appendleft(data)
            elif tmp == self.tail:
                self.append(data)
            else:
                tmp_prev = tmp.prev
                newNode = Node(data, tmp_prev, tmp)
                tmp_prev.next = newNode
                tmp.prev = newNode
        self.size += 1

    # 삭제
    def delete(self, idx):
        if self.is_empty():
            print("underflow")
            return
        else:
            tmp = self.selectNode(idx)
            if tmp == None:
                return
            elif tmp == self.head:
                tmp = self.head
                self.head = self.head.next
            elif tmp == self.tail:
                tmp = self.tail
                self.tail = self.tail.prev
            else:
                tmp.prev.next = tmp.next
                tmp.next.prev = tmp.prev
            del(tmp)
            self.size -= 1

    # 출력
    def printlist(self):
        target = self.head
        while target != self.tail:
            if target.next != self.tail:
                print(target.data, '<=>', end=' ')
            else:
                print(target.data)
            target = target.next

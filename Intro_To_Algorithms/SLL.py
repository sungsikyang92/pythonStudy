class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        # 첫 생성시 내부에는 노드가 없으므로 None이다.

    def listSize(self):
        return self.size

    def is_empty(self):
        if self.size != 0:
            return False
        else:
            return True
    # 노드 현 상황 출력
    def printNode(self):
        if self.head is None: # 데이터가 없을 때
            print("No Data")
            return
        else:
            print("<현재 리스트 구조>", end='\t')
            link = self.head    #처음에는 head를 지정해 줘야 한다. 이후는 next를 지정한다.

            # link가 가리키는 노드가 없을 때까지 반복 해야 하기에 while문을 사용해준다.
            while link:
                print(link.data, '->', end = ' ')
                link = link.next # link를 현 위치 노드의 next로 변경
            print()
    # 노드 추가
    def append(self, data):
        if self.is_empty():
            self.head = Node(data)
            self.size += 1
        else:
            target = self.head
            while target.next != None:
                target = target.next
            newtail = Node(data)
            target.next = newtail
            self.size += 1

    # 삽입
    def insertNode(self, data, idx):
        if self.head is None:    #맨 첫 노드를 저장
            self.head = Node(data)
            self.size += 1
        elif idx == 0:
            self.head = Node(data, self.head)
            self.size += 1
        else:
            target = self.selectNode(idx-1)
            if target == None:
                return
            newNode = Node(data)
            tmp = target.next
            target.next = newNode
            newNode.next = tmp
            self.size += 1

    # 삭제
    def deleteNode(self, idx):
        if self.head is None:
            print("underflow")
            return
        elif idx >= self.size:
            print("overflow")
            return
        elif idx == 0:    # idx == 0을 삭제할 경우 맨 앞의 head를 삭제 하는 것이다.
            target = self.head
            self.head = target.next
            del(target)
            self.size -= 1
        else:
            target = self.selectNode(idx-1)
            deltarget = target.next
            target.next = target.next.next
            del(deltarget)
            self.size -= 1

    # 조회
    def searchNode(self, data):
        if self.head is None:
            print('underflow')
            return
        else:
            link = self.head
            index = 0 # 몇 번째 노드인지 기록하기 위한 index이다.
            while link:
                if data == link.data:
                    return index
                else:
                    link = link.next
                    index += 1

    # 노드선택
    def selectNode(self, idx):
        if idx >= self.size:
            print('overflow')
            return None
        elif idx == 0:
            return self.head
        else:
            target = self.head
            for cnt in range(idx):
                target = target.next
            return target

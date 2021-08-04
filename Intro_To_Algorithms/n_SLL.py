class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class SLL:
    def __init__(self):
        self.head = None
        self.no = 0
        self.current = None

    def len(self):
        return self.no

    def dump(self):
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end=" ")
            ptr = ptr.next

    def search(self, data):
        count = 1
        ptr = self.head
        if ptr is None:
            print("underflow")
        else:
            while ptr.data is not data:
                ptr = ptr.next
                count += 1
            return count
        return " "

    def insert_head(self, data):
        ptr = self.head
        self.head = self.current = Node(data, ptr)
        self.no += 1

    def insert_tail(self, data):
        if self.head is None:
            self.insert_head(data)
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data, None)
            self.no += 1

    def delete_head(self):
        ptr = self.head
        if ptr is None:
            print("underflow")
        else:
            self.head = self.current = self.head.next
        self.no -= 1

    def delete_tail(self):
        if self.head is None:
            print("underflow")
        else:
            if self.head is not None:
                if self.head.next is None:
                    self.delete_head()
                else:
                    pre = self.head
                    ptr = self.head

                    while ptr.next is not None:
                        pre = ptr
                        ptr = ptr.next
                    pre.next = None
                    self.current = pre
                    self.no -= 1

    # def insert_at(self):
    #   원하는 위치에 추가, 나중에 예정
    # def delete_at(self):
    #   원하는 위치에 삭제, 나중에 예정

sll = SLL()
sll.insert_tail(6)
sll.insert_tail(5)
sll.insert_tail(4)
sll.insert_tail(3)
sll.insert_tail(2)
sll.insert_tail(1)
sll.dump()
print()
print(sll.search(6))
print(sll.search(5))
print(sll.search(4))


class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, self.head, None)
        self.no = 0

    def len(self):
        return self.no

    def is_Empty(self):
        if self.no == 0:
            return True
        else:
            return False

    def search_Head(self, data):
        idx = 0
        tmp = self.head
        if tmp is None:
            print("underflow")
        else:
            while tmp.data is not data:
                tmp = tmp.next
                idx += 1
            return idx
        return " "

    def search_Tail(self, data):
        idx = 0
        tmp = self.tail
        if tmp is None:
            print("underflow")
        else:
            while tmp.data is not data:
                tmp = tmp.prev
                idx -= 1
            return idx
        return " "

    def print_all(self):
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end="  ")
            ptr = ptr.next
        print()
    def select_Node(self, idx):
        if idx > self.no:
            print("overflow")
        elif idx == 0:
            return self.head
        elif idx == self.no:
            return self.tail
        elif idx <= (self.no // 2):
            tmp = self.head
            for _ in range(idx):
                tmp = tmp.next
            return tmp
        else:
            tmp = self.tail
            for _ in range(self.no - idx):
                tmp = tmp.prev
            return tmp

    def insert_head(self, data):
        if self.is_Empty():
            self.head = Node(data)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.head
            self.head = Node(data, None, tmp)
            tmp.prev = self.head
        self.no += 1

    def insert_tail(self, data):
        if self.is_Empty():
            self.insert_head(data)
        else:
            tmp = self.tail
            self.tail = Node(data, tmp, None)
            tmp.next = self.tail
            self.tail.prev = tmp
        self.no += 1

    def insert_at(self, data:int, idx:int):
        if self.is_Empty():
            self.insert_head(data)
        else:
            if idx == 0:
                self.insert_head(data)
            elif idx == self.no:
                self.insert_tail(data)
            else:
                tmp = self.select_Node(idx)
                tmp_prev = tmp.prev
                newNode = Node(data, tmp_prev, tmp)
                tmp_prev.next = newNode
                tmp.prev = newNode
        self.no += 1

    def delete_head(self):
        if self.is_Empty():
            print("underflow")
        else:
            self.head = self.head.next
            self.head.prev = None
        self.no -= 1

    def delete_tail(self):
        if self.is_Empty():
            print("underflow")
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.no -= 1

    def delete_at(self, idx):
        if self.is_Empty():
            print("underflow")
        else:
            if self.no == 1:
                self.delete_head()
            elif self.no >= 2:
                tmp = self.select_Node(idx)
                if tmp is self.head:
                    self.delete_head()
                elif tmp is self.tail:
                    self.delete_tail()
                else:
                    tmp.prev.next = tmp.next
                    tmp.next.prev = tmp.prev
        self.no -= 1




dll = DLL()
# dll.insert_head(1)
# dll.insert_head(2)
# dll.insert_head(3)
# dll.insert_tail(4)
# dll.insert_tail(5)
# dll.print_all()
# print()
# print(dll.search_Head(3))
# print(dll.search_Tail(1))
# dll.insert_at(6, 2)
# dll.insert_at(7, 0)
# dll.insert_at(8, 8)
# dll.print_all()
# print()
# dll.delete_head()
# dll.print_all()
# print()
# dll.delete_tail()
# dll.delete_tail()
# dll.print_all()
# print()
# print("*****")
# dll.delete_at(1)
# dll.print_all()
# print()
# print(dll.len())
# print()
# print("******************")
dll.insert_head(1)
dll.insert_head(2)
dll.insert_head(3)
dll.insert_head(4)
dll.insert_head(5)
dll.insert_head(6)
dll.delete_tail()
dll.print_all()
dll.insert_tail(7)
dll.print_all()
dll.delete_at(6)
dll.print_all()
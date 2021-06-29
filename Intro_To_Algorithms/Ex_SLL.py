from SLL import Node
from SLL import SLinkedList

data = SLinkedList()

# data.append(1)
# data.printNode()
print(data.is_empty())
data.printNode()
data.append(1)
data.append(2)
print(data.is_empty())
data.printNode()
print(data.listSize())
data.insertNode(4, 2)
data.insertNode(5, 1)
data.printNode()
data.deleteNode(1)
data.deleteNode(0)
data.printNode()

from DLL import DLL

dll = DLL()

dll.append(4)
dll.append(3)
dll.append(6)
dll.append(8)
dll.printlist()
dll.appendleft(9)
dll.printlist()
dll.delete(0)
dll.printlist()
dll.delete(2)
dll.printlist()
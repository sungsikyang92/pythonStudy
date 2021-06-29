from Queue import Queue

arr = Queue()

# for x in range(1, 10, 2):
#     data.enqueue(x)
#
# print(data)
# print(len(data))
# print(data[0])

arr.enqueue(1)
arr.enqueue(2)
arr.enqueue(3)
print(arr.isEmpty())
print(arr.peek())
arr.dequeue()
print(arr.peek())
arr.dequeue()
print(arr.peek())

for x in range(1, 100, 3):
    arr.enqueue(x)

print(arr.__len__())
print(arr.__str__())
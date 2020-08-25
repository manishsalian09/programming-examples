from queue import Queue

def reverse_elements(queue, k):

    if (queue.empty() or k > queue.qsize()):
        return

    stack = []

    while (len(stack) < k):
        stack.append(queue.get())

    while (len(stack) != 0):
        queue.put(stack.pop())

    for i in range(k):
        queue.put(queue.get())
    
def print_queue(queue):
    while (not queue.empty()):
        print(queue.get(), end = " ")

    print()

queue = Queue(10)
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)
queue.put(6)
queue.put(7)
queue.put(8)
queue.put(9)
queue.put(10)
reverse_elements(queue, 5)
print_queue(queue)

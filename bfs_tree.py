from queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bfs(head):
    queue = Queue();
    
    queue.put(head)
    while (not queue.empty()):
        node = queue.get()

        print(node.data, end = " ")

        if (node.left):
            queue.put(node.left)
        if (node.right):
            queue.put(node.right)

    print()

head = Node(10)
head.left = Node(2)
head.right = Node(15)
head.left.left = Node(1)
head.left.right = Node(7)
head.right.left = Node(14)
head.right.right = Node(16)

bfs(head)

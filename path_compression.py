class Node:
    
    def __init__(self, data):
        self.data = data
        self.parent = None

def compress_path(node):
    if node.parent.data == node.data:
        return node

    node.parent = compress_path(node.parent)
    return node.parent

node4 = Node(10)
node3 = Node(15)
node2 = Node(5)
node1 = Node(1)
node5 = Node(5)
node6 = Node(6)

node4.parent = node3
node2.parent = node3
node3.parent = node1
node1.parent = node5
node5.parent = node5
node6.parent = node1



print(compress_path(node4).data)
print(compress_path(node6).data)


"""
Binary Tree - DFS
                            10
                2                       15
        1               7       14              16

inorder = 1 2 7 10 14 15 16

preorder = 10 2 1 7 15 14 16

postorder = 1 7 2 14 16 15 10
"""

from queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def dfs(head):
    if (head == None): return
    print(head.data, end = " ")
    dfs(head.left)
    dfs(head.right)

head = Node(10)
head.left = Node(2)
head.right = Node(15)
head.left.left = Node(1)
head.left.right = Node(7)
head.right.left = Node(14)
head.right.right = Node(16)

dfs(head)

print()

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None

def construct(arr, i, j, m, n):

    if (i >= m or j >=n ):
        return None

    node = Node(arr[i][j])
    node.right = construct(arr, i, j + 1, m, n)
    node.down = construct(arr, i + 1, j, m, n)
    return node

def display(head):
    if (head == None):
        return None

    node = head
    while (node):

        current = node
        while (current):
            print (current.data, end = " ")
            current = current.right
        print()        
        node = node.down

arr = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

m, n = 3, 3

head = construct(arr, 0, 0, m, n);
display(head)




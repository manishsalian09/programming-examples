import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def add(data):
    node = Node(data)
    node.next = None
    return node

def find_modular_node(head, k):
    if (k < 0 or head == None):
        return None;

    current = head;
    modular_node = None
    while (current):
        if (current.data % k == 0):
            modular_node = current;
        
        current = current.next;

    return modular_node;

head = add(1)
head.next = add(2)
head.next.next = add(3)
head.next.next.next = add(4)
head.next.next.next.next = add(5)
head.next.next.next.next.next = add(6)
head.next.next.next.next.next.next = add(7)
head.next.next.next.next.next.next.next = add(8)
head.next.next.next.next.next.next.next.next = add(9)
head.next.next.next.next.next.next.next.next.next = add(10)

k = 4
modular_node = find_modular_node(head, k);

if (modular_node != None):
    print (modular_node.data)
else:
    print ("N/A")

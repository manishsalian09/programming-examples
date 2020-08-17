from math import sqrt

MAXN = 25
SQRT_SIZE = 5

arr = [0]*(MAXN)
block = [0]*(SQRT_SIZE)
block_size = 0

def preprocess(input, n):
    block_index = -1
    global block_size
    block_size = int(sqrt(n))

    for i in range(n):
        arr[i] = input[i];

        if (i % block_size == 0):
            block_index += 1;

        block[block_index] += arr[i];

def query(l, r):
    sum = 0
    while (l < r and l % block_size != 0 and l != 0):
        sum += arr[l]
        l += 1
    
    while (l + block_size <= r):
        sum += block[l // block_size]
        l += block_size

    while (l <= r):
        sum += arr[l]
        l += 1

    return sum

input = [1, 5, 2, 4, 6, 1, 3, 5, 7]
n = len(input)

preprocess(input, n)

print("query(3, 6)", query(3, 6))
print("query(1, 6)", query(1, 6))
print("query(3, 9)", query(3, 9))

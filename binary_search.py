def search(arr, left, right, number):
    while left <= right:
        median = int((left + right) / 2)
        if arr[median] == number:
            return median
        elif arr[median] < number:
            left = median + 1
        else:
            right = median - 1
    return -1

arr = [3, 6, 1, 66, 11, 5, 100, -1, 0]
arr.sort()
print(arr)
print("number = " + str(66) + ", index = " + str(search(arr, 0, len(arr) - 1, 66)))
print("number = " + str(0) + ", index = " + str(search(arr, 0, len(arr) - 1, 0)))
print("number = " + str(-1) + ", index = " + str(search(arr, 0, len(arr) - 1, -1)))
print("number = " + str(100) + ", index = " + str(search(arr, 0, len(arr) - 1, 100)))


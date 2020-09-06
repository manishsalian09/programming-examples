def find_most_frequent_element(arr):
    element_map = dict()

    for i in range(len(arr)):
        if arr[i] in element_map.keys():
            element_map[arr[i]] += 1
        else:
            element_map[arr[i]] = 1

    print(max(element_map, key = element_map.get))    
            


find_most_frequent_element([1, 2, 1, 4, 5, 5, 7, 8, 4, 5, 6, 7, 5, 7])

def SelectionSort(arr):
    for i in range(len(arr)):
        smallest = min(arr[i:])
        smallest_index = arr[i:].index(smallest) + i
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr

arr = [5,3,6,2,10,2]
print(SelectionSort(arr))
def BinarySearch(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

arr = [1,3,3,7,7]
index = int('1') -1
print(index)
print(BinarySearch(arr, 3))
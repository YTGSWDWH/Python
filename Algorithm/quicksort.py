def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [each for each in arr[1:] if each <= pivot]
        greater = [each for each in arr[1:] if each > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

arr = [10,5,2,3]
print(quicksort(arr))
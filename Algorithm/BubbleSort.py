def BubleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
    return arr

arr = [5,3,6,2,10]
print(BubleSort(arr))
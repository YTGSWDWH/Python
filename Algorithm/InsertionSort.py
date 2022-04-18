def InsertionSort(arr):
    if arr[1] < arr[0]:
        arr[0], arr[1] = arr[1], arr[0]
    for i in range(2,len(arr)):
        for j in range(i):
            if arr[j] <= arr[i] <= arr[j+1]:
                Temp1 = arr[i]
                for m in reversed(range(j+1, i)):
                    arr[m+1] = arr[m]
                arr[j+1] = Temp1
        if arr[i] < arr[0]:
            Temp2 = arr[i]
            for n in reversed(range(0, i)):
                arr[n+1] = arr[n]
            arr[0] = Temp2
    return arr

arr = [5,1,6,2,3]
print(InsertionSort(arr))
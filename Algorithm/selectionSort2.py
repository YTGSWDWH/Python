def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = min(arr)         # 找到最小值
        newArr.append(smallest)     # 将最小值加入新数组
        arr.remove(smallest)        # 将原数组的最小值删掉
    return newArr

arr = [5,3,6,2,10]
print(selectionSort(arr))
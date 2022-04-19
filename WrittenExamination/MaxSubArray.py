def maxSum(arr):
    def reverse(left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    n = len(arr)
    sum1 = 0
    for j in range(n):
        for k in range(j+1,n):
            reverse(j,k)
            b = 0
            for i in range(n):
                if b > 0:
                    b += arr[i]
                else:
                    b = arr[i]
                if b > sum1:
                    sum1 = b
            reverse(j,k)
    return sum1

arr = [-1,3,-5,2,-1,3]
print(maxSum(arr))
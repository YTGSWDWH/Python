def x(nums, k):
    list1 = []
    n = len(nums)
    for i in range(n-k+1):
        list1.append(sum([nums[i+index] for index in range(k)]) / k)
    return list1

k = 5
raw_data = [22.1,22.3,22.4,22.7,22.0,24.0,25.0,27.0,28.0,27.0,29.0,27.0,26.0,25.0,24.0,24.0,23.0,21.0,20.0,22.0]
print(x(raw_data, k))
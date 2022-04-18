nums = [1,12,-5,-6,50,3]
k = 4

max = float('-inf')
for i in range(len(nums) - k + 1):
    if sum([nums[i+index] for index in range(k)]) / k > max:
        max = sum([nums[i+index] for index in range(k)]) / k
        print(max)
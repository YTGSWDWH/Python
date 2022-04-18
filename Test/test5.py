def f(nums):
    time_count = 0
    value_count = 0
    for i in range(nums[0][0]):
        value_max = max(nums[1])
        value_max_index = nums[1].index(value_max)
        value_max_time = nums[2][value_max_index]
        value_max_deadline = nums[3][value_max_index]
        time_max = max(nums[3])
        if (time_count+value_max_time) <= value_max_deadline and (time_count + value_max_time) <= time_max:
            time_count += value_max_time
            value_count += value_max
        nums[1].pop(value_max_index)
        nums[2].pop(value_max_index)
        nums[3].pop(value_max_index)
    return value_count

# nums = [[3],[6,5,4],[5,1,5],[5,5,10]]
nums = [[3],[3,3,10],[1,1,10],[10,10,10]]
print(f(nums))
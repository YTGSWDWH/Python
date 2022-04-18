def findPoisonedDuration(timeSeries, duration):
    count = 0
    for i in range(len(timeSeries)-1):
        if timeSeries[i+1] - timeSeries[i] >= duration:
            count = count + duration
        else:
            count = count + timeSeries[i+1] - timeSeries[i]
    return count + duration

timeSeries = [1,2,3,5]
duration = 2
print(findPoisonedDuration(timeSeries, duration))
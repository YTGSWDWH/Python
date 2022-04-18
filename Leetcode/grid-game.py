def gridGame(grid):
    max_count1 = 0
    max_count2 = 0
    for i in range(len(grid[0])):
        count1 = sum(grid[0][j] for j in range(i+1)) + sum(grid[1][j] for j in range(i,len(grid[0])))
        print(count1)
        if max_count1 < count1:
            max_count1 = count1
            max_index = i
    for i in range(max_index+1):
        grid[0][i] = 0
    for j in range(max_index,len(grid[0])):
        grid[1][j] = 0
    print(grid)
    for i in range(len(grid[0])):
        count2 = sum(grid[0][j] for j in range(i+1)) + sum(grid[1][j] for j in range(i,len(grid[0])))
        max_count2 = max(count2, max_count2)
    return max_count2

grid = [[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]]
print(gridGame(grid))
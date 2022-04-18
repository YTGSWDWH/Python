def islandPerimeter(grid):
    row = len(grid)
    col = len(grid[0])
    count = 0
    num = 0
    for i in range(row):
        for j in range(col-1):
            if grid[i][j] == 1 and grid[i][j] == grid[i][j+1]:
                count = count + 1
    for i in range(row-1):
        for j in range(col):
            if grid[i][j] == 1 and grid[i][j] == grid[i+1][j]:
                count = count + 1
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                num = num + 1
    return num * 4 - count * 2

grid = [[0,1,0,0], [1,1,1,0], [0,1,0,0],[1,1,0,0]]
print(islandPerimeter(grid))
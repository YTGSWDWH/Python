def projectionArea(grid):
    # 这是个注释
    xy = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                xy += 1
    each_row_max = [max(row) for row in grid]
    xz = 0
    for each in each_row_max:
        xz = xz + each
    grid_p = [[row[i] for row in grid] for i in range(len(grid[0]))]
    each_col_max = [max(col) for col in grid_p]
    yz = 0
    for each in each_col_max:
        yz = yz + each
    print(xy,xz,yz)
    return xy + xz + yz

grid = [[1,0],[0,2]]
print(projectionArea(grid))
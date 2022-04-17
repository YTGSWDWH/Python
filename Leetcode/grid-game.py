import copy
def gridGame(grid):
    max_count_min = float('inf')
    for i in range(len(grid[0])):
        grid_1 = copy.deepcopy(grid)
        max_index = i
        max_count = 0
        for i in range(max_index+1):
            grid_1[0][i] = 0
        for j in range(max_index,len(grid[0])):
            grid_1[1][j] = 0
        print(grid_1)
        max_count = max(sum(grid_1[0][index] for index in range(max_index+1,len(grid[0]))),sum(grid_1[1][index] for index in range(max_index)))
        print(max_count)
        max_count_min = min(max_count_min,max_count)
    print(max_count_min)

grid = [[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]]
gridGame(grid)
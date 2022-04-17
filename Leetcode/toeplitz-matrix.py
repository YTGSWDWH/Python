def isToeplitzMatrix(matrix):
    r = len(matrix)
    c = len(matrix[0])
    for nr in range(r):
        for nc in range(c):
            nnr = nr
            nnc = nc
            print(nr,nc)
            while nnr < r-1 and nnc < c-1:
                if matrix[nnr][nnc] != matrix[nnr+1][nnc+1]:
                    return False
                else:
                    nnr = nnr + 1
                    nnc = nnc + 1
    return True

matrix = [[11,74,0,93],[40,11,74,7]]
print(isToeplitzMatrix(matrix))
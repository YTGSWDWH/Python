mat = [[1,2,3],[4,5,6]]

Transpose = [[row[i] for row in mat] for i in range(3)]

Reshape = [[0]*2 for _ in range(3)]
for x in range(2*3):
    Reshape[x // 2][x % 2] = mat[x // 3][x % 3]

print(Transpose)
print(Reshape)
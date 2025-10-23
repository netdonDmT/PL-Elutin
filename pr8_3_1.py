def symm_matrix(matrix):
    for i in matrix:
        if len(i) != len(matrix):
            return False
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True     
matrix1 = [
    [1,2,3],
    [2,5,6],
    [3,6,9]
]
matrix2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(symm_matrix(matrix1))
print(symm_matrix(matrix2))
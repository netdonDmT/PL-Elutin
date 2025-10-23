def divide_matrix(matrix, k):

    n = len(matrix)
    
    if k < 0 or k >= n:
        return None
    
    new_matrix = [row[:] for row in matrix]
    diagonal_element = new_matrix[k][k]
    
    if diagonal_element == 0:
        return None
    
    # Делим элементы k-й строки
    for j in range(n):
        new_matrix[k][j] /= diagonal_element
    
    return new_matrix

matrix1 = [
    [1,2,3],
    [2,5,6],
    [3,6,9]
]
res = divide_matrix(matrix1, 2)

for i in res:
    print(i)
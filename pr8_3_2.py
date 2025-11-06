def max_elem_matrix(matrix):
    
    n = len(matrix)     
    m = len(matrix[0])  
    
    max_value = matrix[0][0]
    max_i, max_j = 0, 0
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_i, max_j = i, j
    
    new_matrix = []
    
    if max_i != 0:
        matrix[0], matrix[max_i] = matrix[max_i], matrix[0]
        if max_j == 0:
            max_j = max_i
        max_i = 0
    
    if max_j != 0:
        for i in range(n):
            matrix[i][0], matrix[i][max_j] = matrix[i][max_j], matrix[i][0]
    
    return matrix

matrix = [
    [1.5, 2.3, 3.7],
    [4.1, 5.9, 6.2],
    [7.8, 8.4, 9.0]
]

result = max_elem_matrix(matrix)
for i in result:
    print(i)
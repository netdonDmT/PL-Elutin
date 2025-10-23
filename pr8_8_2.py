def f(matrix):

    n = len(matrix)
    
    transposed = [[0] * n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            transposed[j][i] = matrix[i][j]
    
    return transposed

# Пример использования
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]



result = f(matrix)


for row in result:
    print(row)
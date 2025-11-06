def f(matrix):
    
    transposed = [[0] * len(matrix) for i in range((len(matrix)))]
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            transposed[j][i] = matrix[i][j]
    
    return transposed

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = f(matrix)

for row in result:
    print(row)
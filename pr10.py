with open("mat1.txt", "r") as f:
    matrix = []
    for line in f:
        r = [int(x) for x in line.split()]
        matrix.append(r)  

def f(matrix):
    transposed = [[0] * len(matrix) for i in range((len(matrix)))]
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            transposed[j][i] = matrix[i][j]
    
    return transposed

res = f(matrix)

with open("mat2.txt", "w") as matrix2:
    for line in res:
        line = str(line)
        matrix2.write(line)




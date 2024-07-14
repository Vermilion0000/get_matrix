def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix

n = 10
m = 10
value = 8
result_matrix = get_matrix(n, m, value)
for row in result_matrix:
    print(row)

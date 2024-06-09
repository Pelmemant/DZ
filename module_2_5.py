def get_matrix(n, m, value):
    matrix = []
    m_matrix = []
    for i in range(m):
        m_matrix.append(value)

    for n in range(n):
        matrix.append(m_matrix)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
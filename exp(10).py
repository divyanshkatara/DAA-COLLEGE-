def add(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(len(X[0]))]
            for i in range(len(X))]


def sub(X, Y):
    return [[X[i][j] - Y[i][j] for j in range(len(X[0]))]
            for i in range(len(X))]


def strassen(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    m = n // 2

    A11 = [row[:m] for row in A[:m]]
    A12 = [row[m:] for row in A[:m]]
    A21 = [row[:m] for row in A[m:]]
    A22 = [row[m:] for row in A[m:]]

    B11 = [row[:m] for row in B[:m]]
    B12 = [row[m:] for row in B[:m]]
    B21 = [row[:m] for row in B[m:]]
    B22 = [row[m:] for row in B[m:]]

    P1 = strassen(A11, sub(B12, B22))
    P2 = strassen(add(A11, A12), B22)
    P3 = strassen(add(A21, A22), B11)
    P4 = strassen(A22, sub(B21, B11))
    P5 = strassen(add(A11, A22), add(B11, B22))
    P6 = strassen(sub(A12, A22), add(B21, B22))
    P7 = strassen(sub(A11, A21), add(B11, B12))

    C11 = add(sub(add(P5, P4), P2), P6)
    C12 = add(P1, P2)
    C21 = add(P3, P4)
    C22 = sub(sub(add(P5, P1), P3), P7)

    return [
        [C11[i][j] + C12[i][j] for j in range(m)]
        for i in range(m)
    ] + [
        [C21[i][j] + C22[i][j] for j in range(m)]
        for i in range(m)
    ]


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print("Result:", strassen(A, B))

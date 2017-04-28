n = 3
test_matrix = [[0] * n for i in range(n)]

test_matrix[0][1] = 1
test_matrix[0][2] = 1
test_matrix[1][0] = -1
test_matrix[2][1] = 1

def pfi(x_i):
    if x_i == 0:
        return -1
    return 1

def get_f_i(i, sign_matrix):
    def f_i(x):
        or_clauses = [(pfi(x[f_i.i]) * pfi(x[j]) * (-1) == sign_matrix[f_i.i][j]) for j in
                      range(len(x))]  # ToDo: Fall i != j
        mu_i = False
        for j in range(len(x)):
            if j == i:
                continue
            elif or_clauses[j] == True:
                mu_i = True
                break
        return (not x[i] and mu_i) or (x[i] and (not mu_i))

    f_i.i = i
    return f_i

def construct_boolean_function(sign_matrix):
    f = [None for _ in range(len(sign_matrix))]
    for i in range(len(sign_matrix)):
        f_i = get_f_i(i, sign_matrix)
        f[i] = f_i
    return f


f = construct_boolean_function(test_matrix)
print((pfi(1) * pfi(0) * (-1) == test_matrix[0][1]))
print([f_i([1,1,1]) for f_i in f])

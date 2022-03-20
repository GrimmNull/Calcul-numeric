import numpy as np


def swap_row(A, i, j):
    A[[i, j]] = A[[j, i]]
    return A


def forwardElimination(A, n):
    for k in range(0, n):
        i_max = k
        v_max = A[i_max][k]
        for i in range(k + 1, n):
            if abs(A[i][k]) > v_max:
                v_max = A[i][k]
                i_max = i
        if A[k][i_max] == 0:
            return k
        if i_max != k:
            swap_row(A, k, i_max)
        for i in range(k + 1, n):
            f = A[i][k] / A[k][k]
            for j in range(k + 1, n + 1):
                A[i][j] -= A[k][j] * f
            A[i][k] = 0
    return -1


def calculateSolution(A, n):
    sol_array = np.empty(n, dtype=np.float64)
    for i in reversed(range(0, n)):
        sol_array[i] = A[i][n]
        for j in range(i + 1, n):
            sol_array[i] -= A[i][j] * sol_array[j]
        sol_array[i] = sol_array[i] / A[i][i]
    print("Solution:")
    print(sol_array)
    return sol_array


def gausian_elemination(A, n):
    singular_flag = forwardElimination(A, n)
    if singular_flag != -1:
        print("Singular matrix")
        if A[singular_flag][n] != 0:
            print("Inconsistent System")
        else:
            print("May have infinitely many solutions")
        return
    print(A)
    return calculateSolution(A, n)


def suma1(l, u, p, i):
    sum = 0
    for k in range(0, p):
        sum += l[p][k]*u[k][i]
    return sum

def suma2(l, u, p, i):
    sum = 0
    for k in range(0, p):
        sum += l[i][k]*u[k][p]
    return sum

def suma3(A, X, i):
    sum = 0
    for j in range(0, i):
        sum += A[i][j]*X[j][0]
    return sum


def suma4(U, X, i):
    sum = 0
    for j in range(i, len(U)):
        sum += U[i][j]*X[j][0]
    return sum
    
def decomp(A):
    L = np.zeros(shape=(len(A), len(A)))
    U = np.zeros(shape=(len(A), len(A)))
    for k, v in enumerate(L):
        for kk, vv in enumerate(v):
            if k == kk:
                L[k][kk] = 1
    for p in range(0, len(A)):
        for i in range(p, len(A)):
            U[p][i] = A[p][i]-suma1(L, U, p, i)
        for i in range(p+1, len(A)):
            L[i][p] = (A[i][p]-suma2(L, U, p, i))/U[p][p]
    return [L, U]

def sol(A, B):
    [L, U] = decomp(A)
    Y = np.zeros(shape=(len(A), 1))
    X = np.zeros(shape=(len(A), 1))
    for i in range(0, len(Y)):
        Y[i][0] = (B[i][0]-suma3(L, Y, i))
    for i in range(len(A)-1, -1, -1):
        X[i][0] = (Y[i][0]-suma4(U, X, i))/U[i][i]
    return X

def rev(A, show_print=True):
    [L, U] = decomp(A)
    Ainvers = np.zeros(shape=(len(A), len(A)))
    for j in range(0, len(A)):
        ej = np.zeros(shape=(len(L), 1))
        ej[j] = 1
        yj = sol(L, ej)
        x = sol(U, yj)
        for i in range(0, len(x)):
            Ainvers[i][j] = x[i][0]
    if(show_print):
        print(Ainvers)
    return Ainvers

def init():
    n = 5
    #A = np.array([ [3.0, 2.0, -4.0, 3.0], [2.0, 3.0, 3.0, 15.0], [5.0, -3, 1.0, 14.0]])
    # A = np.array([ [3.0, 1.0, -3.0, 4.0], [1.0, 3.0, -2.0, -5.0], [2.0, 2.0, 5.0, 7.0]])
    A = np.random.rand(n, n + 1)
    print(A)
    mat_a = np.asmatrix(A[:,[list(range(0,n))]])
    mat_b = np.array(A[:,[n]])
    print("===========Gausian elimination (my alg)==============")
    sol_alg = gausian_elemination(A, n)
    print("===========Gausian elimination (np lib)==============")
    x = np.linalg.solve(mat_a, mat_b)
    print(np.concatenate(x))
    
    print("===========Euclidian norm (np lib)==============")
    dist = np.linalg.norm(sol_alg - np.concatenate(x))
    print(dist)

    # mat_a * sol_alg - mat_b
    print("===========|A init x Gauss - b init|==============")
    y = np.matmul(mat_a, sol_alg)
    z = np.linalg.norm(y - np.concatenate(mat_b))
    print(z)

    print("|xGauss - A^ (-1) bibl b^(init)|")
    a_inv_bilbl = np.linalg.inv(mat_a)
    fiy = np.matmul(a_inv_bilbl, np.concatenate(mat_b))
    res = np.linalg.norm(sol_alg - np.concatenate(fiy))
    print(res)

    print("===========|A gaus^(-1) -  A bibl^(-1)|==============")
    a_inv_alg = rev(np.array(mat_a));
    res = np.linalg.norm(a_inv_alg - a_inv_bilbl)
    print(res)

    
init()

import numpy as np

def swap_row(A,i,j):
    A[[i,j]] = A[[j,i]]
    return A

def forwardElimination(A,n):
    for k in range(0,n):
        i_max = k
        v_max = A[i_max][k]
        for i in range(k+1,n):
            if abs(A[i][k]) > v_max:
                v_max = A[i][k]
                i_max = i
        if A[k][i_max] == 0:
            return k
        if i_max != k:
            swap_row(A,k,i_max)
        for i in range(k+1,n):
            f = A[i][k]/A[k][k]
            for j in range(k+1,n+1):
                A[i][j] -= A[k][j] * f
            A[i][k] = 0
    return -1

def calculateSolution(A,n):
    sol_array = np.empty(n, dtype=np.float64)
    for i in reversed(range(0,n)):
        sol_array[i] = A[i][n]
        for j  in range(i + 1,n):
            sol_array[i] -= A[i][j] * sol_array[j]
        sol_array[i] = sol_array[i] / A[i][i]
    print("Solution:")
    print(sol_array)

def gausian_elemination(A,n):
    singular_flag = forwardElimination(A,n)
    if singular_flag != -1:
        print("Singular matrix")
        if A[singular_flag][n] != 0:
            print("Inconsistent System")
        else:
            print("May have infinitely many solutions")
        return
    print(A)
    calculateSolution(A,n)

def init():
    A = np.array([ [3.0, 2.0, -4.0, 3.0], [2.0, 3.0, 3.0, 15.0], [5.0, -3, 1.0, 14.0]])
    #A = np.array([ [3.0, 1.0, -3.0, 4.0], [1.0, 3.0, -2.0, -5.0], [2.0, 2.0, 5.0, 7.0]])
    n = 3
    gausian_elemination(A,n)
init()
def ex1(x):
    return (1 / 3.0) * pow(x, 2) - 2 * pow(x, 2) + 2 * x + 3


def ex1_der(x):
    return x * x - 4 * x + 2


def f_der(f, x, h):
    # return (3 * f(x) - 4 * f(x - h) + f(x - 2 * h)) / (2 * h)
    return (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)


starting_point = float(input("Starting point: "))
eps = 0.0000001
max_iter = 1000000


def steffensen(g, x0):
    x = x0
    # g = lambda point: f_der(f, point, pow(10, -6))
    del_x = 0
    for i in range(0, max_iter):
        g_diff = g(x + g(x)) - g(x)
        if abs(g_diff) < eps:
            print("Converged after %f iterations", i)
            return x
        del_x = pow(g(x), 2) / g_diff
        x = x - del_x
    if del_x < eps:
        return x
    print('failed to converge in %f iterations' % max_iter)
    return 0


print(ex1_der(2))
print()
g = f_der(ex1, 2, pow(10, -6))
print(g)

ans = steffensen(ex1_der, starting_point)
print("value is: %f" % ans)
print()

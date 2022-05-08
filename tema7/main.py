import random

class PolynomeSolver:
    def __init__(self, path):
        self.eps = 10 ** -6
        self.ai = []
        self.solutions = []

        with open(path, "r") as fin:
            self.ai = [int(x) for x in fin.readline().split()]
            self.solutions = fin.readline().split()

        self.R = (abs(self.ai[0]) + max([abs(x) for x in self.ai[1:]])) / abs(self.ai[0])

    def P(self, x):
        result = 0
        n = len(self.ai)
        for i in range(n):
            result += self.ai[i] * (x ** (n - i - 1))
        return result

    def solve_w_dehghan(self):
        kmax = 10000
        k = 0
        xk = random.uniform(-self.R, self.R)
        delta_x = 1

        xk_orig = xk
        while abs(delta_x) >= self.eps and abs(delta_x) <= 10 ** 8 and k < kmax:
            if abs(self.P(xk)) < self.eps / 10:
                delta_x = 0
            else:
                Pxk = self.P(xk)
                Pxk_plus = self.P(xk + Pxk)
                Pxk_minus = self.P(xk - Pxk)
                yk = xk - ((2 * Pxk * Pxk) / (Pxk_plus - Pxk_minus))
                Pyk = self.P(yk)
                delta_x = 2 * Pxk * (Pxk + Pyk) / (Pxk_plus - Pxk_minus)
            xk = xk - delta_x
            k = k + 1

        if abs(delta_x) < self.eps:
            return xk
        else:
            return None

    def find_all_solutions(self):
        sols = []
        while len(sols) != len(self.solutions):
            result = None
            while result == None:
                result = self.solve_w_dehghan()
            
            exists = False
            for i in range(len(sols)):
                if abs(sols[i] - result) < 0.0001:
                    exists = True
            if abs(self.P(result)) > self.eps:
                continue
            if not exists:
                sols.append(result)
        return sols

ps1 = PolynomeSolver('p1.txt')
# ps2 = PolynomeSolver('p2.txt')
ps3 = PolynomeSolver('p3.txt')
ps4 = PolynomeSolver('p4.txt')

if __name__ == "__main__":
    ps1.solve_w_dehghan()
    # ps2.solve_w_dehghan()
    ps3.solve_w_dehghan()
    ps4.solve_w_dehghan()

    print(ps1.find_all_solutions(), ps1.solutions)
    print(ps3.find_all_solutions(), ps3.solutions)
    print(ps4.find_all_solutions(), ps4.solutions)
    # print(ps2.find_all_solutions(), ps2.solutions)
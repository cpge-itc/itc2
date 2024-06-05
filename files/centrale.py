# Exercice 2
import numpy.random as rd
def X(k, n):
    return [rd.randint(1, n + 1) for _ in range(k)]

# Exercice 4
import scipy.optimize as resol

def x(n):
    def f(x):
        s = 0
        for k in range(1, n + 1):
            s += x**k/k
        return s - 1
    return resol.fsolve(f, 0.5)

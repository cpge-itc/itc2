# Écrire from centrale import * dans votre fichier pour importer toutes les fonctions

# Exercice 1
import scipy.integrate as integr
import numpy as np

def I(x):
    def f(t):
        return t**x/(1 + np.exp(t))
    return integr.quad(f, 0, np.inf)[0]

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

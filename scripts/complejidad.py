import numpy as np
from numba import njit

@njit()
def complejidad(S):
    """
    Calcula la complejidad de una lista de 0 y 1
    Devuelve la complejidad y la complejidad normalizada
    """
    c = 1
    l = 1
    i = 0
    k = 1
    k_max = 1
    n = len(S)
    condicion = True
    while condicion:
        if (S[i+k-1]==S[l+k-1]):
            k += 1
            if (l+k>n):
                c += 1
                condicion = False
        else:
            if (k>k_max):
                k_max = k
            i += 1
            if (i==l):
                c += 1
                l = l + k_max
                i = 0
                k = 1
                k_max = 1
                if (l+1>n):
                    condicion = False
            else:
                k = 1
    b = n/(np.log2(n))
    return c,c/b 
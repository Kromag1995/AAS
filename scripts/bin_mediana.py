import numpy as np
def bin_mediana(s):
    serie_bin_mediana = []
    mediana = np.median(s)
    for i in s:
        if i > mediana:
            serie_bin_mediana.append(1)
        else:
            serie_bin_mediana.append(0)             
    return serie_bin_mediana,mediana

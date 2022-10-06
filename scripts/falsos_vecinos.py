# -*- coding: utf-8 -*-
from pytisean import tiseanio
from .calcular_dE import calcular_dE  
import matplotlib.pyplot as plt
import numpy as np
import time

 
def test_fv(datos, dimension_min=1, dimension_max= 20):
    """
    Funcion para detectar la dimension de embeding usando los falsos primeros vecinos
    La proporcion de primeros vecinos la calcula automaticamente con tisean,
    luego revisa si la proporcion es suficientemente baja para considerarla que llega a 
    la dimensionde embedding 
    Input:
        datos: serie temporal
        dimension_min = dimension minima
        dimension_max = dimension maxima
    Output:
        falsosv: matriz que devuelve tisean, cada fila es un calculo para una dimension,
             las columnas son [dimension, fraccion de falsos primeros vecinos, ...]
        caotico: booleano que indica si se encontro una dimension de embedding
        i+1: la dimension de embedding
    """


    falsosv, msg = tiseanio('false_nearest', '-d1', '-f2', f'-m{dimension_min}', f'-M1,{dimension_max}', data=datos, silent=True)
    caotico = False
    necesito_ver_mas = False
    dim = 5
    print(falsosv)
    if len(falsosv) > 0:
        print(1)
        datos, caotico, neecsito_ver_mas, d_E = calcular_dE(falsosv[:, 1][:dim], variacion_min=0.1,  filtro_fuerte=0.0001, filtro_suave=0.001)
        if not caotico:
            datos, caotico, neecsito_ver_mas, d_E = calcular_dE(falsosv[:,1][:dim], variacion_min=0.1,  filtro_fuerte=0.01, filtro_suave=0.05)
            if not caotico:
                datos, caotico, neecsito_ver_mas, d_E = calcular_dE(falsosv[:,1][:dim],variacion_min = 0.1,  filtro_fuerte  = 0.1, filtro_suave = 0.15)
                if not caotico:
                    dim=20
                    datos, caotico, neecsito_ver_mas, d_E = calcular_dE(falsosv[:,1][:dim],variacion_min = 0.1,  filtro_fuerte  = 0.1, filtro_suave = 0.15)
    else:
        return falsosv, caotico, False, 0, True
    return falsosv, caotico, False, d_E, False

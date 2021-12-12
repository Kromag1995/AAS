# -*- coding: utf-8 -*-
from pytisean import tiseanio
from .calcular_dE import calcular_dE  
import matplotlib.pyplot as plt
import numpy as np
import time

 
def sacar_dE(falsosv):
    caotico = False
    necesito_ver_mas = False
    dim = 5
    if len(falsosv)>0:
        datos,caotico,neecsito_ver_mas,d_E = calcular_dE(falsosv[:,1][:dim],variacion_min = 0.1,  filtro_fuerte =0.0001, filtro_suave = 0.001)
        if not caotico:
            datos,caotico,neecsito_ver_mas,d_E = calcular_dE(falsosv[:,1][:dim],variacion_min = 0.1,  filtro_fuerte = 0.01, filtro_suave = 0.05)
            print(caotico)
            if not caotico:
                datos,caotico,neecsito_ver_mas,d_E = calcular_dE(falsosv[:,1][:dim],variacion_min = 0.1,  filtro_fuerte  = 0.1, filtro_suave = 0.15)
                if not caotico:
                    dim=20
                    datos,caotico,neecsito_ver_mas,d_E = calcular_dE(falsosv[:,1][:dim],variacion_min = 0.1,  filtro_fuerte  = 0.1, filtro_suave = 0.15)
    else:
        return caotico,0, True
    return caotico,d_E, False
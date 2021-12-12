import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from .falsos_vecinos import test_fv 
from .lyapunov import lyapunov
from .sacar_dE import sacar_dE

class bcolors:
    FAIL = '\033[91m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    OKBLUE = '\033[94m'
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def test_caotico():
    """
    Script para calcular la dimension de embedding utilizando primeros vecinos y
    luego calcular los exponentes de lyapunov para determinar la caoticidad del sistema
    """
    input_path = './maximos/Nobinarizados/biinestabilidad/'
    output_path = './falsos vecinos/t=2/'
    output_path_lyap = './lyap/t=2/'
    
    if 'falsos vecinos' not in os.listdir():
        os.mkdir(output_path)
    paso = False
    saltar = False
    archivos_ya_creados = os.listdir(output_path)
    archivos_lyap_ya_creados = os.listdir(output_path_lyap)

    for dirpath,dirname, files in os.walk(input_path):
        for archivo in files:
            if True:
                print(f"{bcolors.OKBLUE}{archivo}{bcolors.ENDC}")
                print(f"{bcolors.OKGREEN}{datetime.now()}{bcolors.ENDC}")
                
                datos = np.genfromtxt(dirpath+'/'+archivo, dtype= None)
                if archivo+"fv" in archivos_ya_creados:
                    continue
                    try:
                        fv = np.loadtxt(output_path+archivo+"fv")[1:]
                        fv = fv.reshape(int(len(fv)/4),4)
                        caotico, d_E, saltar  =  sacar_dE(fv)
                    except Exception as ex:
                        print(ex)
                        continue
                    #print("Saltando: ", output_path+archivo+"fv")
                else:
                    fv, caotico, neecsito_ver_mas, d_E, saltar  =  test_fv(datos, 1, 20)
                    np.savetxt(output_path+archivo+"fv", np.append(d_E, fv) , delimiter=',', header="La primera linea es la dimension de embedding, sigue la matriz de false_nearest")
                if saltar:
                    continue
                print(fv)
                
                if archivo+"lyap" in archivos_lyap_ya_creados:
                    continue
                lyap = 0
                paso =False
                if caotico and d_E >1:
                    print(f"Dimension de embeding : {d_E}" )
                    lyap,paso = lyapunov(datos, d_E)
                    if paso:
                        print("Es Caotico")
                    else:
                        print("No es caotico")
                    if len(lyap)>0:
                        np.savetxt(output_path_lyap+archivo+"lyap", lyap, delimiter=',') 
                else:
                    print("No es caotico")
                    print("Proporcion de falsos vecinos : " + str(fv[d_E-1,1]))

from pytisean import tiseano, tiseanio
import numpy as np
import os


def lyapunov(datos,d_E):
    """
    Calcula los exponentes de Lyapunov
    input: 
        datos : serie temporal
        d_E : dimension de embedding de la serie temporal
    output:
        output: array, el primer elemento es el numero de iteacion, le siguen
            los exponentes de lyapunov y el ultimo elemnto es suma de los exponentes 
    """
    lyap, msg = tiseanio('lyap_spec', f'-m1,{d_E}', data=datos, silent=True)
    print(lyap)
    paso = False
    if len(lyap) != 0:
        try:
            lyapspec=lyap[-1] 
            sum_lyapunov=sum(lyapspec)-lyap[-1][0]
            for ll in lyapspec[1:]:
                if ll>0 and sum_lyapunov<0:
                    paso = True
        except:
            lyapspec=lyap
            sum_lyapunov= sum(lyap) - lyap[0]
            for ll in lyap[1:]:
                if ll>0 and sum_lyapunov<0:
                    paso = True
            print("Paso por except")
    else:
        print("Lyap vacio")
        lyapspec = 0
        sum_lyapunov = 0
    output=np.append(lyapspec,sum_lyapunov)
    del(lyap)
    del(lyapspec)
    del(sum_lyapunov)   
    return output, paso
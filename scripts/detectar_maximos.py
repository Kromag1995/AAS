import numpy as np
from scipy.signal import find_peaks
import os
from scipy.io import loadmat


def detectar_maximos(direccion,distance,height, piso):
    if not  "maximos" in os.listdir():
        os.mkdir("./maximos")
        os.mkdir("./maximos/Nobinarizados")
        os.mkdir("./maximos/Binarizados")
    datos=[]
    for dirpath,dirname, files in os.walk(direccion):
        for i, archivo in enumerate(files):
            if (".mat" in archivo):

                a = loadmat(dirpath+'/'+archivo)
                tira = a['A']
                tiempos = np.arange(0,0.5-a['Tinterval'][0][0],a['Tinterval'][0][0])

                tiempos_cortado = tiempos[::3]
                tira_cortado = tira[::3,0]

                inf = tira_cortado != np.inf
                count_inf = np.sum(tira_cortado == np.inf)
                slices = tira_cortado[inf] > piso
                
                filtrado_V = tira_cortado[slices]/np.max(tira_cortado[slices])
                filtrado_t = tiempos_cortado[slices]

                peaks, _ = find_peaks(filtrado_V,distance = distance, height=height)
                maximos_V = filtrado_V[peaks]
                maximos_t = filtrado_t[peaks]

                #print(f'La cantidad de picos saturados es {count_inf} de {len(filtrado_V)}')
                #print(f'Esto representa %{count_inf*100/len(filtrado_V)}')
                #print(f'La cantidad de picos saturados es {count_inf} de {len(maximos_V)}')
                #print(f'Esto representa %{count_inf*100/len(maximos_V)}')
                archivo = archivo.replace(".mat","")
                np.savetxt(f"./maximos/Nobinarizados/{archivo}_V",maximos_V)

                def_temp = []
                for i in range(1,len(maximos_t)):
                    def_temp.append(maximos_t[i]-maximos_t[i-1])
                maximos_t = def_temp[:]

                np.savetxt(f"./maximos/Nobinarizados/{archivo}_t",maximos_t)

                del(def_temp)
                del(tira)
                del(filtrado_t)
                del(filtrado_V)
                del(maximos_t)
                del(maximos_V)
                del(peaks)
                del(tiempos)
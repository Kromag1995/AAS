import numpy as np
from scipy.signal import find_peaks
import os


def detectar_maximos(direccion, distance, height, piso):
    for dirpath,dirname, files in os.walk(direccion):
        print(dirpath,dirname, files)
        for i, archivo in enumerate(files):
            print(i, archivo)
            if ".csv" in archivo:

                data = np.loadtxt(dirpath+'/'+archivo, delimiter=",", skiprows=3)
                time = data[:, 0]
                volt = data[:, 1]

                inf = volt != np.inf
                count_inf = np.sum(inf)
                slices = volt[inf] > piso

                filter_V = volt[slices]
                filter_T = time[slices]

                peaks, _ = find_peaks(filter_V, distance=distance, height=height)
                max_V = filter_V[peaks]
                max_T = filter_T[peaks]

                #print(f'La cantidad de picos saturados es {count_inf} de {len(filtrado_V)}')
                #print(f'Esto representa %{count_inf*100/len(filtrado_V)}')
                #print(f'La cantidad de picos saturados es {count_inf} de {len(maximos_V)}')
                #print(f'Esto representa %{count_inf*100/len(maximos_V)}')
                archivo = archivo.replace(".csv", "")
                np.savetxt(f"./output/maxs/prebin/{archivo}_V", max_V)

                def_temp = np.diff(max_T)

                np.savetxt(f"./output/maxs/prebin/{archivo}_t", def_temp)

                del def_temp, max_T, max_V, filter_V, filter_T, volt, peaks, time
from pytisean import tiseanio
import os
import numpy as np

archivo =  "20210407-0008_01_V"
carpeta_fv = "falsos vecinos"
carpeta_maximos = ""
sub = "fv"
for i in os.scandir(carpeta_fv):
    if archivo+sub in i.name:
        falsos_v = np.loadtxt(i.path, delimiter=',')
        print(i.path)



datos = np.genfromtxt('maximos/Nobinarizados/'+archivo, dtype=None)

lyap, msg = tiseanio('lyap_spec', f'-m1,2', data=datos)
print(lyap)
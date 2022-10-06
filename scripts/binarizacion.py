import numpy as np
import os
from .complejidad import complejidad
from .utils import binarizarion
from .utils import printProgressBar


def binarizacion(input_dir, output_dir):
    resultados_complejidad = "Nombre del Archivo;Longitud de la cadena;Complejidad_Media;Complejidad_Mediana \n"
    for dirpath,dirname, files in os.walk(input_dir):
        l = len(files)
        if l == 0:
            continue
        printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
        for k, archivo in enumerate(files):
            maximos = np.loadtxt(dirpath+'/'+archivo)  # Carga la serie de maximos de un archivo
            binarios_media,media = binarizarion(maximos, np.mean) #Binarizo la serie
            binarios_mediana,mediana = binarizarion(maximos, np.median)
            largo = len(maximos)
            output_file = open(f'{output_dir}{archivo}_media_{largo}', 'w') # Guardo las serie binarizadas
            stringbin = ''.join([str(num) for num in binarios_media])
            output_file.write(stringbin)
            output_file.close()
            output_file = open(f'{output_dir}{archivo}_mediana_{largo}', 'w')
            stringbin = ''.join([str(num) for num in binarios_mediana])
            output_file.write(stringbin)
            output_file.close()
            complejidad_media = complejidad(binarios_media) # Calculo la complejidad
            complejidad_mediana = complejidad(binarios_mediana)
            "Guarda los resultados en la string"
            resultados_complejidad += f"{archivo};{largo};{complejidad_media[1]};{complejidad_mediana[1]}\n"
            printProgressBar(k + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
            "Elimina las variables que ya no usamos por cuestiones de espacio"
            del maximos
            del binarios_media
            del binarios_mediana


    output_file = open(f'{output_dir}Complejidades.csv', 'w')
    output_file.write(resultados_complejidad)
    output_file.close()

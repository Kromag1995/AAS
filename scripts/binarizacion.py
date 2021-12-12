import numpy as np
import os
from .complejidad import complejidad
from .bin_media import bin_media
from .bin_mediana import bin_mediana
from .utils import printProgressBar


def binarizacion(direccion):
    resultados_Complejidad = "Nombre del Archivo;Longitud de la cadena;Complejidad_Media;Complejidad_Mediana \n"
    dir_output = './maximos/Analisis Salto Binarizacion media mediana/Binarizacion/'
    for dirpath,dirname, files in os.walk(direccion):
        l = len(files)
        if l == 0:
            continue
        printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
        for k,archivo in enumerate(files):
            if archivo != "0009t":
                continue
            maximos = np.loadtxt(dirpath+'/'+archivo)  # Carga la serie de maximos de un archivo
            binarios_media,media = bin_media(maximos) #Binarizo la serie
            binarios_mediana,mediana = bin_mediana(maximos)
            largo = len(maximos)
            output_file = open(f'{dir_output}{archivo}_media_{largo}', 'w') # Guardo las serie binarizadas
            stingbin = ''.join([str(num) for num in binarios_media])
            output_file.write(stingbin)
            output_file.close()
            output_file = open(f'{dir_output}{archivo}_mediana_{largo}', 'w')
            stingbin = ''.join([str(num) for num in binarios_mediana])
            output_file.write(stingbin)
            output_file.close()
            complejidad_media = complejidad(binarios_media) # Calculo la complejidad
            complejidad_mediana = complejidad(binarios_mediana)
            "Guarda los resultados en la string"
            resultados_Complejidad += f"{archivo};{largo};{complejidad_media[1]};{complejidad_mediana[1]}\n"
            printProgressBar(k + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
            "Elimina las variables que ya no usamos por cuestiones de espacio"
            del(maximos)
            del(binarios_media)
            del(binarios_mediana)


    output_file = open(f'{dir_output}Complejidades.txt', 'w')
    output_file.write(resultados_Complejidad)
    output_file.close()
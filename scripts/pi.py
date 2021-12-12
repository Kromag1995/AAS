import numpy as np
import os
from complejidad import complejidad
from bin_media import bin_media
from bin_mediana import bin_mediana




resultados_Complejidad = "Nombre del Archivo;Longitud de la cadena;Media;Complejidad_Media(c,c/b);Mediana;Complejidad_Mediana(c,c/b) \n"

"Carga la serie de maximos de un archivo"
archivo = open('./pi')
maximos =  archivo.read()
archivo.close()
maximos = np.array(list(maximos.replace('.',''))).astype(int)
binarios_media,media = bin_media(maximos)
binarios_mediana,mediana = bin_mediana(maximos)
output_file = open(f'./maximos/binarizacion/pi_media_{len(binarios_media)}.bin', 'w')
stingbin = ''.join([str(num) for num in binarios_media])
output_file.write(stingbin)
output_file.close()
output_file = open(f'./maximos/binarizacion/pi_mediana{len(binarios_mediana)}.bin', 'w')
stingbin = ''.join([str(num) for num in binarios_mediana])
output_file.write(stingbin)
output_file.close()
"Calcula la complejidad"
complejidad_media = complejidad(binarios_media)
complejidad_mediana = complejidad(binarios_mediana)
"Guarda los resultados en la string"
resultados_Complejidad += f"pi;{len(binarios_media)};{media};{str(complejidad_media)};{mediana};{str(complejidad_mediana)}\n"
"Elimina las variables que ya no usamos por cuestiones de espacio"
del(maximos)
del(binarios_media)
del(binarios_mediana)


output_file = open('Resultados3.txt', 'w')
output_file.write(resultados_Complejidad)
output_file.close()

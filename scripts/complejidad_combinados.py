import os
from .complejidad import complejidad

def complejidad_combinados():
    archivos = os.walk('./maximos/Bits_salteados/')
    for dirpath,dirnames,filenames in archivos:
        if "Salto" in dirpath:
            for file in sorted(filenames):
                if not ("csv" in file):
                    serie = open(dirpath+'/'+file,'r').read()
                    compleji = complejidad(serie)
                    print(dirpath+'/'+file, compleji)
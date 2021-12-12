import os
import functools
from .utils import printProgressBar


from randomness_testsuite.ApproximateEntropy import ApproximateEntropy as aet
from randomness_testsuite.Complexity import ComplexityTest as ct
from randomness_testsuite.CumulativeSum import CumulativeSums as cst
from randomness_testsuite.FrequencyTest import FrequencyTest as ft
from randomness_testsuite.BinaryMatrix import BinaryMatrix as bm
from randomness_testsuite.Matrix import Matrix as mt
from randomness_testsuite.RandomExcursions import RandomExcursions as ret
from randomness_testsuite.RunTest import RunTest as rt
from randomness_testsuite.Serial import Serial as serial
from randomness_testsuite.Spectral import SpectralTest as st
from randomness_testsuite.TemplateMatching import TemplateMatching as tm
from randomness_testsuite.Universal import Universal as ut





def test_all():

    path_to_input = './maximos/Bits_salteados/'

    test_function = {
        0:[ft.monobit_test, 100, 1], 
        1:[ft.block_frequency, 100, 1],
        2:[rt.run_test, 100, 1],
        3:[rt.longest_one_block_test, 128, 1], 
        #4:[mt.binary_matrix_rank_text, 38_912, 1],
        5:[st.sepctral_test, 1000, 1],
        6:[tm.non_overlapping_test, 10, 1],
        #7:[tm.overlapping_patterns, 1_000_000, 1],
        #8:[ut.statistical_test, 387000, 1],
        #9:[ct.linear_complexity_test, 1_000_000, 1],
        #10:[serial.serial_test, 10, 2],
        #11:[aet.approximate_entropy_test, 10, 1],
        #12:[cst.cumulative_sums_test, 100, 1],
        #13:[functools.partial(cst.cumulative_sums_test, mode=1), 100, 1],
        #14:[ret.random_excursions_test, 1000000, 8],
        #15:[ret.variant_test, 1000000, 11]
    }

    all_results = {}
    for dirpath,dirname, files in os.walk(path_to_input):#Direcion de los archivos binarizados
        printProgressBar(0, len(files), prefix = 'Progress:', suffix = 'Complete', length = 50)
        for i,archivo in enumerate(files):
            if "csv" in archivo:
                continue
            input_file = open(os.path.join(dirpath,archivo), 'r')#Direcion de los archivos binarizados
            data = input_file.read()
            results = [len(data)]
            for test in test_function.values():
                if len(data) >= test[1]:
                    asd = test[0](data)
                    if type(asd) == list:
                        for tupla in asd:
                            results.append(tupla[-2:][0])
                    elif type(asd[0]) == tuple:
                        results.append(asd[0])
                        results.append(asd[1])
                    else:
                        results.append(asd[0])
                else:
                    for ii in range(test[2]):
                        results.append(("NC","NC"))
            all_results[f'{dirpath[-7:]+"_"+archivo}']= results
            printProgressBar(i+1, len(files), prefix = 'Progress:', suffix = 'Complete', length = 50)
    output = """Archivo;n;01. Frequency Test (Monobit);02. Frequency Test within a Block;03. Run Test;04. Longest Run of Ones in a Block; 06. Discrete Fourier Transform (Spectral) Test;07. Non-Overlapping Template Matching Test\n"""

    for result in all_results.keys():
        resultados = f"{result}"
        for rr in all_results[result]:
            resultados += f";{rr}"
        output += resultados + "\n"

    output_file = open(path_to_input+'datosMarcelo.csv', 'w')
    output_file.write(output)
    output_file.close()
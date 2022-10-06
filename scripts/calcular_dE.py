

def calcular_dE(datos, variacion_min, filtro_fuerte, filtro_suave):
    caotico = False
    necesito_ver_mas = False
    fv_anterior = 100
    for i in range(len(datos)):

        if datos[i] < filtro_fuerte:
            caotico = True
            necesito_ver_mas = False
            break
        else:
            if fv_anterior == 100:
                fv_anterior = datos[i]
            else:
                variacionfv = 1 - datos[i]/fv_anterior
                if variacionfv < -0.1:
                    caotico = False
                    necesito_ver_mas = False
                    break
                elif variacionfv < variacion_min and datos[i] < filtro_suave:
                    caotico = True
                    necesito_ver_mas = False
                    break
                fv_anterior = datos[i]
    return datos,caotico,False,i+1
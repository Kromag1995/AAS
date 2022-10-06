import click
from scripts.detectar_maximos import detectar_maximos
from scripts.binarizacion import binarizacion
from scripts.test_caotico import test_caotico


def seleccion_de_procesos():
    """
    Funcion para seleccionar que procesos correr
    """
    procesos_disponibles = [
        "Filtrado de datos",
        "Deteccion de maximos",
        "Binarizacion por estadistica",
        "Test de aleatoriedad",
        "Test de caoticidad",
        "Filtrar maximos segun salto"]
    procesos_seleccionados = []
    t = "".join(f"[{i}] {p}\n" for i,p in enumerate(procesos_disponibles))
    click.prompt(f"seleccione que proceso correr\n{t}")
    t += f"[R] Imprimir esta lista\n"
    while True:
        p = click.prompt(f"Seleccione el siguiente proceso, de no haber mas entre [Q]\n{t}").upper()
        if p == "Q":
            break
        procesos_seleccionados.append(p)
    return procesos_seleccionados


@click.command()
def main():
    detectar_maximos("./input", 20, 0.5, 0.01)
    binarizacion("./output/maxs/prebin/", "./output/maxs/bin/")
    test_caotico()


if __name__ == '__main__':
    main()
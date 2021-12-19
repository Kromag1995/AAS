import click

def seleccion_de_procesos():
    """
    Funcion para seleccionar que procesos correr
    """
    procesos_disponibles = ["Filtrado de datos", "Deteccion de maximos", "Binarizacion por estadistica",
                            "Test de aleatoriedad", "Test de caoticidad", "Filtrar maximos segun salto"]
    procesos_seleccionados = []
    t = "".join(f"[{i}] {p}\n" for i,p in enumerate(procesos_disponibles))
    procesos_seleccionados.append(
        click.prompt(f"seleccione que proceso correr\n{t}")
    )
    t += f"[R] Imprimir esta lista\n"
    while True:
        p = click.prompt(f"Seleccione el siguiente proceso, de no haber mas entre [Q]\n{t}").upper()
        if p == "Q":
            break
        procesos_seleccionados.append(p)
    return procesos_seleccionados


@click.command()
def main():
    print("Bienvenido a AAS")
    tareas_a_procesar = seleccion_de_procesos()
    print(tareas_a_procesar)

if __name__ == '__main__':
    main()
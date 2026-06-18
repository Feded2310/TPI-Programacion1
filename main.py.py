import csv
import os
 
ARCHIVO_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "paises.csv")
 
 
# LECTURA Y ESCRITURA DEL CSV
 
 
def cargar_paises():
    """Lee el archivo CSV y devuelve una lista de diccionarios."""
    paises = []
    try:
        with open(ARCHIVO_CSV, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }
                    paises.append(pais)
                except (ValueError, KeyError):
                    print(f"Fila con formato incorrecto ignorada: {fila}")
    except FileNotFoundError:
        print(f"No se encontró el archivo '{ARCHIVO_CSV}'. Se iniciará con lista vacía.")
    return paises
 
 
def guardar_paises(paises):
    """Guarda la lista de diccionarios en el archivo CSV."""
    with open(ARCHIVO_CSV, newline="", encoding="utf-8", mode="w") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(paises)
 
 
# AGREGAR PAÍS
 
 
def agregar_pais(paises):
    """Solicita los datos de un nuevo país y lo agrega a la lista."""
    print("\nAgregar país")
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
 
    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print("Ya existe un país con ese nombre.")
            return
 
    try:
        poblacion = int(input("Población: ").strip())
        superficie = int(input("Superficie (km²): ").strip())
    except ValueError:
        print("Población y superficie deben ser números enteros.")
        return
 
    continente = input("Continente: ").strip()
    if not continente:
        print("El continente no puede estar vacío.")
        return
 
    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(pais)
    guardar_paises(paises)
    print(f"País '{nombre}' agregado correctamente.")
 
 
# ACTUALIZAR PAÍS
 
 
def actualizar_pais(paises):
    """Actualiza población y superficie de un país existente."""
    print("\nActualizar país")
    nombre = input("Nombre del país a actualizar: ").strip()
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            try:
                nueva_poblacion = int(input(f"Nueva población (actual: {pais['poblacion']}): ").strip())
                nueva_superficie = int(input(f"Nueva superficie (actual: {pais['superficie']}): ").strip())
            except ValueError:
                print("Debe ingresar números enteros.")
                return
            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie
            guardar_paises(paises)
            print(f"País '{nombre}' actualizado correctamente.")
            return
    print(f"No se encontró el país '{nombre}'.")
 
 
# BUSCAR PAÍS
 
 
def buscar_pais(paises):
    """Busca países por nombre (coincidencia parcial o exacta)."""
    print("\nBuscar país")
    termino = input("Ingrese nombre o parte del nombre: ").strip().lower()
    if not termino:
        print("Debe ingresar un término de búsqueda.")
        return
    resultados = [p for p in paises if termino in p["nombre"].lower()]
    if resultados:
        print(f"\nSe encontraron {len(resultados)} resultado(s):")
        mostrar_tabla(resultados)
    else:
        print("No se encontraron países con ese nombre.")
 
 
# FILTRAR PAÍSES
 
 
def filtrar_paises(paises):
    """Submenú para filtrar países por continente, población o superficie."""
    print("\nFiltrar países")
    print("1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")
    opcion = input("Opción: ").strip()
 
    if opcion == "1":
        continente = input("Continente: ").strip()
        if not continente:
            print("Debe ingresar un continente.")
            return
        resultados = [p for p in paises if p["continente"].lower() == continente.lower()]
 
    elif opcion == "2":
        try:
            minimo = int(input("Población mínima: ").strip())
            maximo = int(input("Población máxima: ").strip())
        except ValueError:
            print("Debe ingresar números enteros.")
            return
        resultados = [p for p in paises if minimo <= p["poblacion"] <= maximo]
 
    elif opcion == "3":
        try:
            minimo = int(input("Superficie mínima (km²): ").strip())
            maximo = int(input("Superficie máxima (km²): ").strip())
        except ValueError:
            print("Debe ingresar números enteros.")
            return
        resultados = [p for p in paises if minimo <= p["superficie"] <= maximo]
 
    else:
        print("Opción inválida.")
        return
 
    if resultados:
        print(f"\n{len(resultados)} país/es encontrado(s):")
        mostrar_tabla(resultados)
    else:
        print("No se encontraron países con esos criterios.")
 
 
# ORDENAR PAÍSES
 
 
def ordenar_paises(paises):
    """Ordena y muestra los países según el criterio elegido."""
    print("\nOrdenar países")
    print("1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")
    opcion = input("Opción: ").strip()
 
    criterios = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    if opcion not in criterios:
        print("Opción inválida.")
        return
 
    clave = criterios[opcion]
 
    if opcion == "1":
        descendente = False
    else:
        orden = input("Orden (1=Ascendente / 2=Descendente): ").strip()
        descendente = orden == "2"
 
    ordenados = sorted(paises, key=lambda p: p[clave], reverse=descendente)
    mostrar_tabla(ordenados)
 
 
# ESTADÍSTICAS
 
 
def mostrar_estadisticas(paises):
    """Calcula y muestra estadísticas generales del dataset."""
    if not paises:
        print("No hay países cargados.")
        return
 
    print("\nEstadísticas")
 
    mayor_pob = max(paises, key=lambda p: p["poblacion"])
    menor_pob = min(paises, key=lambda p: p["poblacion"])
    promedio_pob = sum(p["poblacion"] for p in paises) // len(paises)
 
    mayor_sup = max(paises, key=lambda p: p["superficie"])
    menor_sup = min(paises, key=lambda p: p["superficie"])
    promedio_sup = sum(p["superficie"] for p in paises) // len(paises)
 
    continentes = {}
    for p in paises:
        c = p["continente"]
        continentes[c] = continentes.get(c, 0) + 1
 
    print(f"\nPoblación:")
    print(f"  Mayor:    {mayor_pob['nombre']} ({mayor_pob['poblacion']:,})")
    print(f"  Menor:    {menor_pob['nombre']} ({menor_pob['poblacion']:,})")
    print(f"  Promedio: {promedio_pob:,}")
 
    print(f"\nSuperficie:")
    print(f"  Mayor:    {mayor_sup['nombre']} ({mayor_sup['superficie']:,} km²)")
    print(f"  Menor:    {menor_sup['nombre']} ({menor_sup['superficie']:,} km²)")
    print(f"  Promedio: {promedio_sup:,} km²")
 
    print(f"\nPaíses por continente:")
    for continente, cantidad in sorted(continentes.items()):
        print(f"  {continente}: {cantidad}")
 
 
# MOSTRAR TABLA
 
 
def mostrar_tabla(paises):
    """Muestra una lista de países en formato de tabla."""
    print()
    print(f"{'Nombre':<20} {'Población':>15} {'Superficie (km²)':>18} {'Continente':<12}")
    print("-" * 67)
    for p in paises:
        print(f"{p['nombre']:<20} {p['poblacion']:>15,} {p['superficie']:>18,} {p['continente']:<12}")
    print()
 
 
# MENÚ PRINCIPAL
 
 
def menu():
    """Muestra el menú principal y gestiona la navegación."""
    paises = cargar_paises()
    while True:
        print("\nGESTIÓN DE DATOS DE PAÍSES")
        print("1. Agregar país")
        print("2. Actualizar país")
        print("3. Buscar país")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Estadísticas")
        print("7. Mostrar todos los países")
        print("0. Salir")
        opcion = input("Opción: ").strip()
 
        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            filtrar_paises(paises)
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "7":
            mostrar_tabla(paises)
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida. Ingrese un número del 0 al 7.")
 
 
# ENTRADA AL PROGRAMA
 
if __name__ == "__main__":
    menu()

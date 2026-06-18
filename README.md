# Gestión de Datos de Países en Python

Aplicación de consola desarrollada en Python que permite gestionar información sobre países. El sistema lee datos desde un archivo CSV y ofrece funcionalidades de búsqueda, filtrado, ordenamiento y estadísticas.

---

## Integrantes

- Federico Javier Doello

---

## Requisitos

- Python 3.x
- Los archivos `main.py` y `paises.csv` deben estar en la misma carpeta.

---

## Cómo ejecutar el programa

1. Descargar o clonar el repositorio.
2. Asegurarse de que `main.py` y `paises.csv` estén en la misma carpeta.
3. Abrir una terminal en esa carpeta y ejecutar:

```
python main.py
```

---

## Funcionalidades

| Opción | Descripción |
|--------|-------------|
| 1 | Agregar un nuevo país |
| 2 | Actualizar población y superficie de un país |
| 3 | Buscar país por nombre (parcial o exacto) |
| 4 | Filtrar por continente, rango de población o superficie |
| 5 | Ordenar por nombre, población o superficie |
| 6 | Ver estadísticas generales |
| 7 | Mostrar todos los países |
| 0 | Salir |

---

## Ejemplos de uso

### Mostrar todos los países
```
Opción: 7

  Nombre                     Población   Superficie (km²) Continente
  -------------------------------------------------------------------
  Argentina                 45,376,763          2,780,400 América
  Brasil                   213,993,437          8,515,767 América
  ...
```

### Buscar un país
```
Opción: 3
Ingrese nombre o parte del nombre: ar

  Nombre                     Población   Superficie (km²) Continente
  -------------------------------------------------------------------
  Argentina                 45,376,763          2,780,400 América
  Marruecos                 36,910,560            446,550 África
```

### Filtrar por continente
```
Opción: 4
  1. Por continente
  2. Por rango de población
  3. Por rango de superficie
Opción: 1
Continente: Asia

  Nombre                     Población   Superficie (km²) Continente
  -------------------------------------------------------------------
  China               1,412,600,000          9,596,960 Asia
  India               1,380,004,385          3,287,263 Asia
  Japón                 125,800,000            377,975 Asia
```

### Estadísticas
```
Opción: 6

  Población:
    Mayor:    China (1,412,600,000)
    Menor:    Australia (25,499,884)
    Promedio: 327,194,919

  Superficie:
    Mayor:    Rusia (17,098,242 km²)
    Menor:    Reino Unido (243,610 km²)
    Promedio: 3,878,826 km²

  Países por continente:
    África: 4
    América: 6
    Asia: 3
    Europa: 5
    Oceanía: 1
```
## Estructura del repositorio

```text
📁 TPI-Programacion/
│
├── main.py
├── paises.csv
├── README.md
└── TPI programacion1.pdf
```


## Video demostrativo

[Ver video demostrativo](https://www.youtube.com/watch?v=JotQwvfoVkg&t=3s)


## Documentación PDF

El informe se encuentra disponible en este repositorio como archivo:
- TPI programacion1.pdf

## Repositorio

[https://github.com/Feded2310/TPI-Programacion1](https://github.com/Feded2310/TPI-Programacion1)

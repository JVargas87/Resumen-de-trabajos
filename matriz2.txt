import numpy as np

# Matriz proporcionada
matriz = np.array([
    [20, 50, 50, 102],
    [11, 52, 41, 7],
    [3, 41, 62, 81],
    [28, 1, 37, 20],
    [15, 49, 61, 35],
    [9, 56, 28, 90],
    [79, 3, 41, 32],
    [51, 9, 74, 84],
    [4, 73, 20, 48],
    [58, 48, 67, 142],
    [74, 18, 35, 61]
])

# Función para calcular la suma de una submatriz sin contar la fila, columna y el elemento elegido
def suma_submatriz_sin_fila_columna(matriz, i1, j1, i2, j2, fila, columna):
    """Calcula la suma de la submatriz desde (i1, j1) hasta (i2, j2) sin incluir fila, columna y celda elegida."""
    suma = 0
    for i in range(i1, i2 + 1):
        for j in range(j1, j2 + 1):
            if i != fila and j != columna:  # Ignorar la fila, columna y celda elegida
                suma += matriz[i, j]
    return suma

# Función para encontrar el elemento que divide la matriz en 4 zonas iguales
def encontrar_elemento_igual_suma(matriz):
    m, n = matriz.shape
    for i in range(1, m):  # Iterar desde la fila 1 hasta la penúltima
        for j in range(1, n):  # Iterar desde la columna 1 hasta la penúltima
            # Sumar las cuatro zonas sin contar la fila, columna y celda elegida
            zona1 = suma_submatriz_sin_fila_columna(matriz, 0, 0, i-1, j-1, i, j)  # Arriba izquierda
            zona2 = suma_submatriz_sin_fila_columna(matriz, 0, j, i-1, n-1, i, j)  # Arriba derecha
            zona3 = suma_submatriz_sin_fila_columna(matriz, i, 0, m-1, j-1, i, j)  # Abajo izquierda
            zona4 = suma_submatriz_sin_fila_columna(matriz, i, j, m-1, n-1, i, j)  # Abajo derecha
            
            # Verificar si las cuatro zonas tienen la misma suma
            if zona1 == zona2 == zona3 == zona4:
                return (i, j), zona1  # Devuelve la posición y la suma de las zonas
    return None, None  # Si no se encuentra ningún elemento que cumpla la condición

# Buscar el elemento
posicion, suma = encontrar_elemento_igual_suma(matriz)

if posicion:
    print(f"El elemento en la posición {posicion} divide la matriz en cuatro zonas con una suma de {suma}.")
else:
    print("No se encontró ningún elemento que divida la matriz en cuatro zonas con igual suma.")

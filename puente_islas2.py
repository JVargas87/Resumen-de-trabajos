# Crear la matriz vacía de 11x9 (filas x columnas)
mapa = [[" " for _ in range(9)] for _ in range(11)]

# Definir las celdas de la isla A
isla_A = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
          (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
          (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
          (4, 1), (4, 2), (4, 3), (4, 4), 
          (5, 5)]

# Definir las celdas de la isla B
isla_B = [(8, 5), (8, 6), (8, 7), (8, 8), (8, 9),
          (9, 5), (9, 6), (9, 7), (9, 8), (9, 9),
          (10, 5), (10, 6), (10, 7), (10, 8), (10, 9),
          (11, 5), (11, 6), (11, 7), (11, 8), (11, 9)]

# Marcar las celdas de la isla A en la matriz
for x, y in isla_A:
    mapa[x - 1][y - 1] = "A"

# Marcar las celdas de la isla B en la matriz
for x, y in isla_B:
    mapa[x - 1][y - 1] = "B"

# Imprimir el mapa
print("Mapa inicial:")
print("  1 2 3 4 5 6 7 8 9")  # Encabezado de columnas
for i, fila in enumerate(mapa):
    print(f"{i + 1} " + " ".join(fila))

# Calcular la distancia Manhattan entre los puntos específicos (4,4) y (8,9)
punto_especifico_A = (4, 4)
punto_especifico_B = (8, 9)
distancia_especifica = abs(punto_especifico_B[0] - punto_especifico_A[0]) + abs(punto_especifico_B[1] - punto_especifico_A[1])

print("\nCálculo de distancia específica:")
print(f"La distancia entre los puntos {punto_especifico_A} (Isla A) y {punto_especifico_B} (Isla B) es: {distancia_especifica}")

# Calcular la distancia mínima entre las dos islas
distancia_minima = float('inf')  # Inicialmente infinito
punto_cercano_A = None
punto_cercano_B = None

for a in isla_A:  # Para cada punto en isla A
    for b in isla_B:  # Para cada punto en isla B
        distancia = abs(a[0] - b[0]) + abs(a[1] - b[1])
        if distancia < distancia_minima:
            distancia_minima = distancia
            punto_cercano_A = a
            punto_cercano_B = b

# Imprimir los resultados del cálculo general
print("\nCálculo de distancia mínima entre las islas:")
print(f"La menor distancia entre las islas A y B es: {distancia_minima}")
print(f"Punto más cercano en isla A: {punto_cercano_A}")
print(f"Punto más cercano en isla B: {punto_cercano_B}")

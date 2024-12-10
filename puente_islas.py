# Coordenadas de las celdas con "A" y "B"
isla_A = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
          (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
          (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
          (4, 1), (4, 2), (4, 3), (4, 4), 
          (5, 5)]

isla_B = [(8, 5), (8, 6), (8, 7), (8, 8), (8, 9),
          (9, 5), (9, 6), (9, 7), (9, 8), (9, 9),
          (10, 5), (10, 6), (10, 7), (10, 8), (10, 9),
          (11, 5), (11, 6), (11, 7), (11, 8), (11, 9)]

# Inicializamos la distancia mínima con un valor alto
distancia_minima = float('inf')
punto_A = None
punto_B = None

# Calculamos la distancia Manhattan entre cada par de puntos
for a in isla_A:
    for b in isla_B:
        distancia = abs(a[0] - b[0]) + abs(a[1] - b[1])
        if distancia < distancia_minima:
            distancia_minima = distancia
            punto_A = a
            punto_B = b

# Resultados
print(f"Menor distancia: {distancia_minima}")
print(f"Punto en isla A: {punto_A}")
print(f"Punto en isla B: {punto_B}")

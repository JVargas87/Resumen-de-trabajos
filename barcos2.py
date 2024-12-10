# Revisión del algoritmo para corregir el cálculo de orientación y extremos de los barcos.

def obtener_barcos(MAT):
    filas = len(MAT)
    columnas = len(MAT[0])
    visitadas = [[False for _ in range(columnas)] for _ in range(filas)]

    def dfs(x, y):
        # Direcciones posibles: horizontal, vertical y diagonal
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        barco = [(x, y)]
        stack = [(x, y)]
        visitadas[x][y] = True
        
        while stack:
            cx, cy = stack.pop()
            for dx, dy in direcciones:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < filas and 0 <= ny < columnas and MAT[nx][ny] == 1 and not visitadas[nx][ny]:
                    visitadas[nx][ny] = True
                    barco.append((nx, ny))
                    stack.append((nx, ny))
        
        return barco

    barcos = []
    for i in range(filas):
        for j in range(columnas):
            if MAT[i][j] == 1 and not visitadas[i][j]:
                barcos.append(dfs(i, j))

    resultados = []
    for barco in barcos:
        if len(barco) > 1:  # Solo barcos mayores a una celda
            barco = sorted(barco)  # Ordena celdas del barco para determinar extremos
            inicio = (barco[0][0] + 1, barco[0][1] + 1)
            fin = (barco[-1][0] + 1, barco[-1][1] + 1)
            resultados.append(f"Existe un barco de tamaño {len(barco)} entre la celda {inicio[0]},{inicio[1]} y la celda {fin[0]},{fin[1]}")

    return resultados


# Matriz de prueba
MAT = [
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
]

# Ejecución
resultados = obtener_barcos(MAT)
for resultado in resultados:
    print(resultado)

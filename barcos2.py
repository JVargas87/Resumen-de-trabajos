def obtener_barcos(MAT):
    filas = len(MAT)
    columnas = len(MAT[0])
    visitadas = [[False for _ in range(columnas)] for _ in range(filas)]

    def dfs(x, y, barco):
        # Dirección de movimientos: horizontal, vertical y diagonal
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        barco.append((x, y))
        visitadas[x][y] = True
        
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas and MAT[nx][ny] == 1 and not visitadas[nx][ny]:
                dfs(nx, ny, barco)

    barcos = []
    
    for i in range(filas):
        for j in range(columnas):
            if MAT[i][j] == 1 and not visitadas[i][j]:
                barco = []
                dfs(i, j, barco)
                barcos.append(barco)

    resultados = []
    for barco in barcos:
        if len(barco) > 1:  # Solo consideramos barcos que ocupan más de una celda
            # Determinar la orientación del barco
            xs = [celda[0] for celda in barco]
            ys = [celda[1] for celda in barco]
            
            min_x, max_x = min(xs), max(xs)
            min_y, max_y = min(ys), max(ys)

            # Detectar si es horizontal, vertical o diagonal
            if min_x == max_x:  # Horizontal
                inicio = (min_x + 1, min_y + 1)
                fin = (max_x + 1, max_y + 1)
            elif min_y == max_y:  # Vertical
                inicio = (min_x + 1, min_y + 1)
                fin = (max_x + 1, max_y + 1)
            else:  # Diagonal
                inicio = (min_x + 1, min_y + 1)
                fin = (max_x + 1, max_y + 1)

            resultados.append(f"Existe un barco de tamaño {len(barco)} entre la celda {inicio[0]},{inicio[1]} y la celda {fin[0]},{fin[1]}")
    
    return resultados


# Ejemplo de uso
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

resultados = obtener_barcos(MAT)
for resultado in resultados:
    print(resultado)

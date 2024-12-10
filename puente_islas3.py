from flask import Flask, jsonify, request

app = Flask(__name__)

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

# Marcar las celdas de las islas en la matriz
for x, y in isla_A:
    mapa[x - 1][y - 1] = "A"

for x, y in isla_B:
    mapa[x - 1][y - 1] = "B"

@app.route('/mapa', methods=['GET'])
def obtener_mapa():
    """
    Devuelve el mapa de las islas A y B.
    """
    return jsonify({"mapa": mapa})

@app.route('/distancia-especifica', methods=['POST'])
def calcular_distancia_especifica():
    """
    Calcula la distancia Manhattan entre dos puntos específicos.
    """
    datos = request.get_json()
    punto_A = datos.get("punto_A")  # Ejemplo: [4, 4]
    punto_B = datos.get("punto_B")  # Ejemplo: [8, 9]
    
    if not punto_A or not punto_B:
        return jsonify({"error": "Se deben enviar los puntos A y B"}), 400

    distancia = abs(punto_B[0] - punto_A[0]) + abs(punto_B[1] - punto_A[1])
    return jsonify({
        "punto_A": punto_A,
        "punto_B": punto_B,
        "distancia": distancia
    })

@app.route('/distancia-minima', methods=['GET'])
def calcular_distancia_minima():
    """
    Calcula la distancia mínima entre las islas A y B.
    """
    distancia_minima = float('inf')
    punto_cercano_A = None
    punto_cercano_B = None

    for a in isla_A:
        for b in isla_B:
            distancia = abs(a[0] - b[0]) + abs(a[1] - b[1])
            if distancia < distancia_minima:
                distancia_minima = distancia
                punto_cercano_A = a
                punto_cercano_B = b

    return jsonify({
        "distancia_minima": distancia_minima,
        "punto_cercano_A": punto_cercano_A,
        "punto_cercano_B": punto_cercano_B
    })

if __name__ == '__main__':
    app.run(debug=True)

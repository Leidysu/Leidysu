# Matriz de 3 x 3
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(matriz)

# Función buscar_valor específico
def buscar_valor(matriz,valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return i, j
    return None  # En caso de que el valor no se encuentre

valor_buscado = 9
posicion = buscar_valor(matriz, valor_buscado)

if posicion:
    print("Valor encontrado en la posición", posicion)
else:
    print("Valor no encontrado")
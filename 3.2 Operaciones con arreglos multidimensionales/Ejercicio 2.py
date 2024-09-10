# Ejercicio 2 matriz de 3x3
matriz = [[3, 6, 9],
          [12, 15, 18],
          [21, 24, 27]]

print("Matriz original:")
print(matriz)

# Método de ordenamiento bubble_sort
def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(n-1, i, -1):
            if fila[j] < fila[j-1]:
                fila[j], fila[j-1] = fila[j-1], fila[j]
                print(fila)

# Ordenar cada fila de la matriz utilizando bubble_sort
for fila in matriz:
    bubble_sort(fila)

print("Matriz ordenada:")
print(matriz)


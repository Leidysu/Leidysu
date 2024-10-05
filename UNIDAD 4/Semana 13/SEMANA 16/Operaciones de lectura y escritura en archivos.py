#  Operaciones de lectura y escritura en archivos
# Definimos el nombre del archivo
file_name = "my_notes.txt"

# Modo de apertura: "w" para escritura (write)
archivo_escritura = open (file_name,"w")

# Escribo tres líneas de notas personales
archivo_escritura.write("Línea 1: Me encanta la fragancia de las rosas.\n")
archivo_escritura.write("Línea 2: Aprecio las cosas simples de la vida.\n")
archivo_escritura.write("Línea 3: Pienso que hay que aprovechar cada día como si no quedase mañana.\n")
archivo_escritura.write("Línea 4: Enseñar es brindar la luz que alumbrará mi camino, gracias por guiarme y darme tus conocimientos para un buen futuro.\n")

# Cerramos el archivo de escritura
archivo_escritura.close()

# Modo de apertura: "r" para lectura (read)
archivo_lectura = open(file_name, "r")

# Metodo readline() lee una línea a la vez
archivo_lectura.seek(0)
linea_1 = archivo_lectura.readline()
linea_2 = archivo_lectura.readline()
linea_3 = archivo_lectura.readline()
linea_4 = archivo_lectura.readline()

print("\n Contenido linea por linea usando readline ():")
print(linea_1.strip())
print(linea_2.strip())
print(linea_3.strip())
print(linea_4.strip())


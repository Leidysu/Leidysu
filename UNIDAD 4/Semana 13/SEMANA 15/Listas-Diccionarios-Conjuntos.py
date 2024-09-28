# Creación de una lista
from idlelib.editor import keynames

números=[1,2,3,"cuatro",5.0 ]
print(números)
print(números[0])
print(números[1])
print(números[2])
print(números[3])
print(números[4])
números.append(10)
print(números)



# Eliminar elementos en una lista
números.remove("cuatro")
print(números)

# Ejemplo con diccionario
persona ={
    "nombre":"Leidy",
    "apellido":"Pazmiño",
    "edad":29,
    "sexo":"F",

}
# Obtener valores
print(persona)
print("nombre:",persona ["nombre"])
print("apellido:",persona ["apellido"])
print("edad:",persona ["edad"])
print("sexo:",persona ["sexo"])

# Modificar clave
persona ["edad"]= 39
print("nombre:",persona ["nombre"])
print("apellido:",persona ["apellido"])
print("edad:",persona ["edad"])
print("sexo:",persona ["sexo"])

# Agregar un nuevo par-clave
persona ["profesion"]="Diseñadora Gráfica"
print("todo:",persona)

# Eliminar un nuevo par-clave
del persona ["sexo"]
print("todo:",persona)

# Imprime las claves
claves=persona.keys()
print("Imprime las claves",claves )

# Imprime valor
valores=persona.values()
print("Imprime los valores",valores)

# Recorrer con un for
for clave, valor in persona.items():
    print (clave,":",valor)

# Conjuntos de cosméticos
cosméticos= {"rimel,labial,maquillaje,perfume"}
print(cosméticos)

# Añadir un elemento
cosméticos.add("brillo")
print(cosméticos)
# Eliminar un elemento
cosméticos.discard("perfume")
print(cosméticos)

# Añadir un elemento
cosméticos.add("delineador")
print(cosméticos)

cosméticos.add("sombras")
print(cosméticos)
cosméticos.add("rubor")
print(cosméticos)
cosméticos.discard("sombras")
print(cosméticos)
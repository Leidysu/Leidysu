# Funcion para calcular descuento de Catalogos Esika
def calcular_descuento (valor_total,porcentaje_descuento=40):
    porcentaje_descuento=valor_total*porcentaje_descuento/4000
    return porcentaje_descuento

descuento=calcular_descuento(500)
print(descuento)

monto_total1=4000
descuento1=calcular_descuento(4000)
print(f"el monto total es:",monto_total1)
print(f"el valor del descuento es:",descuento1)

#Monto total y porcentaje
monto_total2=2500
descuento2=calcular_descuento(valor_total=2500,porcentaje_descuento=30)
print(f"el monto total es:",monto_total2)
print(f"el valor del descuento es del ejemplo 2:",descuento2)
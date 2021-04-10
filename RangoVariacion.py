print("Escribir un programa en el cual: dada una lista de tres valores numericos distintos se calcule e informe su rango de variacion (debe mostrar el mayor y el menor de ellos)")
print("***********************************************************************************************************************")
print("***********************************************************************************************************************")
print("***********************************************************************************************************************")
first= int(input("Ingresa el primer valor:"))
second= int(input("Ingresa el segundo valor:"))
third= int(input("Ingresa el tercer valor:"))


if first > second:
    if first> third: 
        mayor=first
    else:
        mayor=third

else: 
    if second >third:
        mayor= second
    else: 
        mayor = third

if first < second:
    if first < third: 
        minor= first
    else:
        minor=third
        
else: 
    if second < third:
        minor= second
    else: 
        minor = third


print(f"El rango de los numero es: [{minor},{mayor}], de los numeros ingresados: {first},{second},{third}")















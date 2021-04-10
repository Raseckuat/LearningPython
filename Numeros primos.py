print("Desarrollar un programa que permita cargar n numeros enteros y luego nos informe cuantos valores fueron pares y cuantos impares. Emplear el operador “%” en la condicion de la estructura condicional (este operador retorna el resto de la division de dos valores, por ejemplo 11%2 retorna un 1):")
flag=1
counter=0
par=0
impar=0
while flag==1:
    
    if (int(input("Por favor ingrese un numero:")))%2==0:
        par+=1
    else:
        impar+=1
    counter+=1
    if int(input("Desea seguir ingresando numeros? Digite 0 para NO u otro numero para continuar.."))==0:
        flag=0
    else: 
        flag=1

print(f"La cantidad de numeros ingresados fue:{counter}, Los pares fueron:{par} y los impares:{impar} ")

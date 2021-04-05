numero=int(input("Ingresa un numero entre 1 y 99:"))
if numero >0 and numero <25:
    if numero < 9:
        print(f"El numero= {numero}, tiene 1 digito")

    else: 
        print(f"El numero= {numero}, tiene 2 digito")

else:
    print(f"el numero= {numero}, esta fuera de rango.")
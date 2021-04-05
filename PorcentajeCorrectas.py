print("Bienvendo a el programa de porcentajes")
tot_preg=int(input("Favor ingresar el total de preguntas:"))
correctas=int(input("Ingrese el total de correctas:"))

if(correctas > tot_preg): 
    print("El numero de correctas NO puede ser mayor que las correctas.")
else:
    porcentaje=int((correctas/tot_preg)*100)
    #print(f"Porcentajes: {porcentaje}")
    if porcentaje >= 90:
        print(f"El promedio del evaluado es:{porcentaje}%, tiene Nivel Maximo.")
    
    elif porcentaje >= 75 and porcentaje < 90:
        print(f"El promedio del evaluado es:{porcentaje}%, tiene Nivel Medio.")

    elif porcentaje >= 50 and porcentaje < 75:
        print(f"El promedio del evaluado es:{porcentaje}%, tiene Nivel Regular.")

    else: 
        print(f"El promedio del evaluado es:{porcentaje}%, Fuera de nivel.")

        
            
        





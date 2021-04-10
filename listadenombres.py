""" Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuantos de esos nombres tienen 5 o más caracteres.
"""
lista=["uno", "dos", "tres", "cuatro", "cinco"]
contador=0
for i in range(len(lista)):
    lista[i]=input(f"Ingrese el nombre #{i+1}:")
    if len(lista[i])>=5:
        contador+=1
print(f"El total de nombres con 5 o mas de 5 caracteres es:{contador}")

contador=0
for i in lista:
    i=input(f"Ingrese el nombre #:")
    if len(i)>=5:
        contador+=1
print(f"El total de nombres con 5 o mas de 5 caracteres es:{contador}")

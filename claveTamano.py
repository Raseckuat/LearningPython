"""Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres. Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, en caso contrario mostrar un mensaje de error."""

clave="default"
while len(clave)<10 or len(clave)>20:
        if clave!="default":
            print("Error: La clave debe tener entre 10 y 20 caracteres")
            
        clave=input("Ingrese la clave, esta debe tener entre 10 y 20 caracteres:")
        
print(f"La clave es:{clave}")
          
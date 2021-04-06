print("Se cuenta con la siguiente información:")
print("Las edades de 5 estudiantes del turno mañana.")
print("Las edades de 6 estudiantes del turno tarde.")
print("Las edades de 11 estudiantes del turno noche.")
print("Las edades de cada estudiante deben ingresarse por teclado.")
print("a) Obtener el promedio de las edades de cada turno (tres promedios)")
print("b) Imprimir dichos promedios (promedio de cada turno) ")
print("c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.")

temp=0
pmanana=0
ptarde=0
pnoche=0


print("Estudiantes de la manana:")
for i in range(1,6):
    temp+=int(input(f"Please enter the Edad {i}:"))
pmanana=temp/5
print(f"El promedio de edades de los estudiantes de manana es={pmanana}")

print("*****************************************************************")

print("Estudiantes de la Tarde:")
temp=0
for i in range(1,7):
    temp+=int(input(f"Please enter the Edad {i}:"))
ptarde=temp/6
print(f"El promedio de edades de los estudiantes de manana es={ptarde}")

print("*****************************************************************")

print("Estudiantes de la Noche:")
temp=0
for i in range(1,12):
    temp+=int(input(f"Please enter the Edad {i}:"))
pnoche=temp/6
print(f"El promedio de edades de los estudiantes de manana es={pnoche}")

if pmanana > ptarde and pmanana > pnoche:
        print(f"El promedio de edades de la manana es mayor, ya que es:{pmanana}")
elif ptarde > pnoche:
       print(f"El promedio de edades de la tarde es mayor, ya que es:{ptarde}")

else:
       print(f"El promedio de edades de la noche es mayor, ya que es:{pnoche}")

input("Presione cualquier tecla para terminar.")


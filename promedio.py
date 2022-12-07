"""
    Calcula el promedio de una lista de N datos
"""

print("Ingrese la cantidad de datos:")
n = int(input())
acum = 0
for i in range(1,n+1):
	print("Ingrese el dato ",i,":")
	dato = float(input())
	acum = acum+dato
prom = acum/n
print("El promedio es: ",prom)

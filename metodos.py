
# funcion que no recibe ni devuelve nada
def saludar():
	print("Hola mundo!")

# funcion que recibe un argumento por valor, y devuelve su doble
def calculardoble(num):
	# retorna el doble
	res = num*2
	return res

# funcion que recibe un argumento por referencia, y lo modifica
def triplicar(num):
	# modifica la variable duplicando su valor
	num = num*3

# proceso principal, que invoca a las funciones antes declaradas
if __name__ == '__main__':
	print("Llamada a la funcion Saludar:") # como no recibe argumentos pueden omitirse los paréntesis vacios
	saludar()
	print("Ingrese un valor numérico para x:")
	x = input()
	print("Llamada a la función CalcularDoble (pasaje por valor)")
	print("El doble de ",x," es ",calculardoble(x))
	print("El valor original de x es ",x)
	print("Llamada a la función Triplicar (pasaje por referencia)")
	triplicar(x)
	print("El nuevo valor de x es ",x)

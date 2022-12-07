
""" 
    Declara un arreglo de 10 elementos 
"""

import random

a=[] 
for i in range(0,10):
    elementos=random.randint(1,99)
    a.append(elementos)
print("Los elementos del arreglo son:",a)
print("") # deja una linea en blanco

for i in reversed(a):
    print("En orden inverso:",i," ", end="\n")

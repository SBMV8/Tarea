"""
    Muestra como hacer un menú simple con las estructuras Repetir-Hasta Que y Según
"""

opc=True
while opc:
    print("Menú de Recomendaciones\n")
    print("1. Literatura\n2. Cine\n3. Música\n4. Videojuegos\n5. Salir")

    opc=input("Ingrese una opcion (1-5): ") 
    if opc=="1": 
      print("\nLecturas recomendables:\n") 
      print("+ Esperándolo a Tito y otros cuentos de fútbol (Eduardo Sacheri)\n")
      print("+ El juego de Ender (Orson Scott Card)\n")
      print("+ El sueño de los héroes (Adolfo Bioy Casares)\n")
    elif opc=="2":
      print("\nPelículas recomendables:\n") 
      print("+ Matrix (1999)\n")
      print("+ El último samuray (2003)\n")
      print("+ Cars (2006)\n")
    elif opc=="3":
      print("\nDiscos recomendables:\n") 
      print("+ Despedazado por mil partes (La Renga, 1996)\n")
      print("+ Búfalo (La Mississippi, 2008)\n")
      print("+ Gaia (Mägo de Oz, 2003)\n")
    elif opc=="4":
      print("\nVideojuegos clásicos recomendables:\n") 
      print("+ Día del tentáculo (LucasArts, 1993)\n")
      print("+ Terminal Velocity (Terminal Reality/3D Realms, 1995)\n")
      print("+ Death Rally (Remedy/Apogee, 1996)\n")
    elif opc=="5":
      print("\nGracias, vuelva pronto\n") 
    elif opc!="":
      print("\nOpción no válida\n") 
      break

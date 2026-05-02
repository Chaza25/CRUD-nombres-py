nombres = []
apellidos = []
edades = []

def agregarPersonas(nombre, apellido, edad):
    nombres.append(nombre)
    apellidos.append(apellido)
    edades.append(edad)
    print("\nPersona agregada con exito!")

def eliminarPersona(nombre):
    if nombre in nombres:
        indice = nombres.index(nombre)
        nombres.pop(indice)
        apellidos.pop(indice)
        edades.pop(indice)
        print(f"{nombre} ha sido eliminado")
    else:
        print(f"{nombre} no se econtro en la lista")

def modificarPersona(nombre, nuevoNombre, nuevoApellido, nuevaEdad):
    if nombre in nombres:
        indice = nombres.index(nombre)
        nombres[indice] = nuevoNombre
        apellidos[indice] = nuevoApellido
        edades[indice] = nuevaEdad
        print(f"La informacion de {nombre} ha sido actualizada")
    else:
        print(f"No se encontro a {nombre} en la informacion")

def buscarPersona(nombre):
    if nombre in nombres:
        indice = nombres.index(nombre)
        print(f"Nombre: {nombres[indice]}, Apellido: {apellidos[indice]}, Edad: {edades[indice]}")
    else: 
        print(f"{nombre} no se encontro en la lista")

def imprimirPersonas(nombre, apellido, edad):
    print("Nombre: ", nombres)
    print("Apellido: ", apellidos)
    print("Edad: ", edades)
    print(f"Actualmente hay {len(nombres)} personas en la lista.\n")

print("Ingrese 1 para agregar una persona\nIngrese 2 para eliminar\nIngrese 3 para modificar\nIngrese 4 para buscar\nIngrese 5 para ver las listas")
print()

opcion = int(input("Ingrese una opcion del 1 al 5\nIngrese 6 para salir: "))
print()

while opcion != 6:
    if opcion == 1:
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        edad = int(input("Ingrese la edad: "))
        agregarPersonas(nombre, apellido, edad)
    elif opcion == 2:
        nombre = input("Ingrese el nombre de la persona que desea elimar de las listas: ")
        eliminarPersona(nombre)
    elif opcion == 3:
        nombre = input("Ingrese el nombre de la persona que desea modificar: ")
        nuevoNombre = input("Ingrese la modificacion del nombre: ")
        nuevoApellido = input("Ingrese la modificacion del apellido: ")
        nuevaEdad = input("Ingrese la modificacion de la edad: ")
        modificarPersona(nombre, nuevoNombre, nuevoApellido, nuevaEdad)
    elif opcion == 4:
        nombre = input("Ingrese el nombre de la persona que esta buscando: ")
        buscarPersona(nombre)
    elif opcion == 5:
        imprimirPersonas(nombre, apellido, edad)
    elif opcion == 6:
        print("Saliendo del programa...")
    else:
        print()
        print("Ingreso una opcion no deseada, vuelva a ingresar una opcion del 1 al 6")
    
    print("Ingrese 1 para agregar una persona\nIngrese 2 para eliminar\nIngrese 3 para modificar\nIngrese 4 para buscar\nIngrese 5 para ver las listas")
    print()
    opcion = int(input("Ingrese una opcion del 1 al 5\nIngrese 6 para salir: "))
    print() 
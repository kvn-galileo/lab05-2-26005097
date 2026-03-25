# Ejercicio #4: (Nombre del archivo: ejercicio4.py)
# Para este ejercicio se le pide que implemente lo siguiente:

# (1) Lea un numero N de usuario.
# (2) Si el numero es entero y mayor que 0 :
# Genere N numeros aleatorios entre 10 y 99,
# y metalos en una lista, ordenados ascendentemente.
# (3) Conforme va generando un numero aleatorio nuevo, debe desplegar el
# numero generado y desplegar la lista con el numero ya ordenado, todo esto debe hacerse en orden.
# Para este ejercicio puede usar whiles y fors como le convenga. Recuerde que puede definir ciclos,
# dentro de ciclos. NO DEBE UTILIZAR NINGUNA FUNCION QUE ORDENE LA LISTA.
# Ejemplo:
# 		Ingrese un numero N: 5
# 		Numero #1 generado: 11
# 		[11]
# 		Numero #2 generado: 34
# 		[11, 34]
# 		Numero #3 generado: 26
# 		[11, 26, 34]
# 		Numero #4 generado: 72
# 		[11, 26, 34, 72]
# 		Numero #5 generado: 15
# 		[11, 15, 26, 34, 72]
import random

try:
    n = int(input("Ingrese N: "))

    sorted_list = []

    for i in range(1, n + 1):
        random_number = random.randint(10, 99)

        if len(sorted_list) == 0:
            sorted_list.append(i)
            print(sorted_list)
            continue
        
        resorted_list = []
        for index in range(0, len(sorted_list) - 1):
            current = sorted_list[index]

            if random_number >= current:
                resorted_list.append(random_number)
            else:
                resorted_list.insert(sorted_list.indexof(current), random_number)

        sorted_list = resorted_list

        print(sorted_list)
        


except ValueError:
    print("El valor ingresado no es un numero")
	
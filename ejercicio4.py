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

    random_numbers = []
    for i in range(1, n + 1):
        new_random_number = random.randint(10, 99)
        random_numbers.append(new_random_number)

        print(f"Numero #1 generado: {new_random_number}")

        sorted_arr = []

        for conteo in range(0, len(random_numbers)):
            if (len(random_numbers) <= 0):
                break

            current = random_numbers[0]
            lower = current
            index_lower = None

            indice_actual = 0
            for current_n in random_numbers:
                if lower >= current_n:
                    lower = current_n
                    index_lower = indice_actual
                indice_actual += 1

            new_arr = []
            index = 0
            # creacion de filter
            while index != len(random_numbers):
                item = random_numbers[index]

                if (index != index_lower):
                    new_arr.append(item)

                index += 1
            
            random_numbers = new_arr
            sorted_arr.append(lower)

        random_numbers = sorted_arr
        print(random_numbers)


except ValueError:
    print("El valor ingresado no es un numero")
	
# Ejercicio #3: (Nombre del archivo: ejercicio3.py)
# Usted esta trabajando para una empresa de juegos educativos para niños. 
# Para la primera fase de uno de los juegos, 
# le piden que haga un programa en Python que traduzca numeros en palabras.
# Su programa debe hacer lo siguiente:

# (1) Debe tener la lista de los numeros del 0 al 9 en palabras ya predefinida.
# (2) Cuando empiece el programa, debe leer un numero en forma de String.
# (3) Debe leer cada digito, uno a uno, del numero leido y traducirlo a letras utilizando la lista predefinida
# (4) Desplegar los numeros en letras, separados por espacios, en una sola linea.
# (5) Terminar el programa
# Ejemplos:
# 			Ingrese numero: 1234
# 			Respuesta: uno dos tres cuatro


# 			Ingrese numero: 48037
# 			Respuesta: cuatro ocho cero tres siete

number_word_list = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
result_list = []
numeros = input("Ingrese numero: ")

for index in range(0, len(numeros)):
    current_n = numeros[index]
    if current_n.isnumeric():
        n_index = int(current_n) - 1
        current_word = number_word_list[n_index]
        result_list.append(current_word)
    else:
        print(current_n, " is not a number.")
        continue

valor = " ".join(result_list)
print(valor)


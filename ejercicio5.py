# Ejercicio #5: (Nombre del archivo: ejercicio5.py)
# Escriba un programa en Python, que lea una palabra del usuario
# y despliegue si la palabra es un palindromo o no. Recuerde que un 
# palindromo se lee igual del principio a fin, que al reves. 
# Debe implementar este proceso manualmente utilizando ciclos 
# y no algo que ya le haga el trabajo en una instrucción.
# Use while o for o listas si necesita.

user_word = input("Ingrese una palabra: ")
word = user_word.strip().replace(' ', '').lower()
print(user_word)

backward = len(word) - 1
esPalindromo = True
for n in range(len(word) // 2):
    current = word[n]
    last_one = word[backward]

    if (current != last_one):
        esPalindromo = False
        break
    else:
        backward-=1
        continue

if (esPalindromo):
    print("Es palindromo")
else:
    print("No es palindromo")

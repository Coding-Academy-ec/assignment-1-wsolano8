"""
Ejercicio 1: Suma de Dos Números
Descripción: Este ejercicio consiste en crear una función que reciba dos números como argumentos y devuelva la suma de ambos.
"""

def sumar(a, b):
    # Escribe aqui el return de la suma de 2 numeros
    suma = a + b
    return suma

"""
Ejercicio 2: Factorial de un Número
Descripción: En este ejercicio se requiere crear una función que calcule el factorial de un número dado. El factorial de un número nn se calcula como n!=n×(n−1)×(n−2)×…×1n!=n×(n−1)×(n−2)×…×1.
"""
    
def factorial(n):
    if n == 0:
        # Escribe aqui el return de la operacion anterior
        resul = "No es Factorial"
    else:
        # Escribe aqui el return de la operacion contraria a la operacion anterior
        factorial = 1
        i = 1
        while (i <= n):
            factorial = factorial * i
            i = i + 1
    resul = n
    return resul

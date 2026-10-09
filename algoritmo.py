def sumar_hasta_n(n):
    suma = 0
    contador = 1

    while contador <= n:
        suma = suma + contador
        contador = contador + 1

    return suma


n = int(input("Introduce un número: "))
print("La suma es:", sumar_hasta_n(n))
def palindromo(x):
    if x < 1 or x > 10000:
        return False

    # Convertimos el número en una lista de dígitos
    digitos = []
    while x > 0:
        digitos.append(x % 10)
        x = x // 10

    # Usamos dos punteros para recorrer la lista
    i, j = 0, len(digitos) - 1
    while i < j:
        if digitos[i] != digitos[j]:
            return False
        i += 1
        j -= 1

    return True

# Ejemplos de uso
print(es_palindromo(121))  # Verdadero
print(es_palindromo(100))  # Falso
print(es_palindromo(0))    # Falso
print(es_palindromo(12321))  # falso
print(es_palindromo(-121))  # falso

def numDuplicado(A):
    if not A:
        return 0

    k = 1  # Inicializamos k en 1 porque siempre habrá al menos un elemento único
    for i in range(1, len(A)):
        if A[i] != A[k - 1]:  # Comparamos con el último único encontrado
            A[k] = A[i]  # Almacenamos el nuevo elemento único
            k += 1  # Incrementamos k

    return k

# Ejemplo de uso
A = [1, 1, 2, 2, 3, 4, 4, 5]
k = numDuplicado(A)
print(f"El número de elementos únicos es: {k}")
print(f"Los elementos únicos son: {A[:k]}")
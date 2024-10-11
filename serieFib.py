def fibonacci(n):
    # Creamos un diccionario para almacenar los números de Fibonacci
    fib_dict = {0: 0, 1: 1}

    # Calculamos los números de Fibonacci y los almacenamos en el diccionario
    for i in range(2, n):
        fib_dict[i] = fib_dict[i - 1] + fib_dict[i - 2]

    return fib_dict

# Número de términos de la serie de Fibonacci que queremos generar y aqui termina la ejecucion del algoritmo
n = 12
resultado = fibonacci(n)

# Aqui solo se imprimen los resultados con los valores n esimos solicitados para ser visualizados
for i in range(n):
    print(f"Fibonacci({i}) = {resultado[i]}")

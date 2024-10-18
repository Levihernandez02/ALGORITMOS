def palindromo(x):
    # Verificamos que x esté en el rango permitido
    if x < 1 or x > 10000:
        return False

    # Variables para almacenar la longitud y los dígitos
    temp = x
    longitud = 0
    
    # Contar cuántos dígitos tiene el número
    while temp > 0:
        temp //= 10
        longitud += 1

    # Usamos dos punteros para comparar dígitos
    i = 10 ** (longitud - 1)  # Mayor potencia de 10 para el primer dígito
    j = 1  # Menor potencia de 10 para el último dígito

    while i > j:  # Comparar hasta el medio
        primer_digito = (x // i) % 10  # Obtiene el primer dígito
        ultimo_digito = (x // j) % 10   # Obtiene el último dígito

        if primer_digito != ultimo_digito:
            return False  # Si los dígitos no coinciden, no es un palíndromo

        # Desplazamos los punteros hacia el interior
        i //= 10
        j *= 10

    return True  # Si todos los dígitos coinciden, es un palíndromo

# Solicitar al usuario un número
try:
    x = int(input("Introduce un número entero entre 1 y 10000: "))
    if palindromo(x):
        print(f"{x} es un palíndromo.")
    else:
        print(f"{x} no es un palíndromo.")
except ValueError:
    print("Por favor, introduce un número entero válido.")
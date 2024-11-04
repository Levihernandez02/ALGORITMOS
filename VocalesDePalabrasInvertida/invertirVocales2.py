def invertir_vocales(s):
    # Se le asigna a la variable vocales una cadena con el conocimiento de las vocales
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    lista_cadena = list(s)
    i, j = 0, len(s) - 1
    
    while i < j:
        if lista_cadena[i] in vocales and lista_cadena[j] in vocales:
            lista_cadena[i], lista_cadena[j] = lista_cadena[j], lista_cadena[i]
            i += 1
            j -= 1
        if lista_cadena[i] not in vocales:
            i += 1
        if lista_cadena[j] not in vocales:
            j -= 1

    # Construir la cadena 
    cadena_resultante = ""
    for caracter in lista_cadena:
        cadena_resultante += caracter

    return cadena_resultante

# Ejemplo de uso
cadena = "sistemas"
cadena1 = "algoritmos"
cadena2 = "computacion"
cadena3 = "diamante"
cadena4 = "lapiz"

print(invertir_vocales(cadena))  # Imprime sastemis
print(invertir_vocales(cadena1))  # Imprime olgirotmas
print(invertir_vocales(cadena2))  # Imprime compitacuon
print(invertir_vocales(cadena3))  # deamanti
print(invertir_vocales(cadena4))  # lipaz

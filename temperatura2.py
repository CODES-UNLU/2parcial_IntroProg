def es_temperatura_valida(entrada):
    """Verifica si la entrada es un número entero entre -18 y 50 inclusive."""
    if len(entrada) == 0:
        return False

    if entrada[0] == '-' and entrada[1:].isdigit():
        valor = int(entrada)
    elif entrada.isdigit():
        valor = int(entrada)
    else:
        return False

    return -18 <= valor <= 50

def pedir_temperatura():
    while True:
        entrada = input("Ingresá una temperatura entre -18 y 50: ")
        if es_temperatura_valida(entrada):
            print(f"Temperatura aceptada: {entrada}°C")
            break
        else:
            print("Temperatura inválida. Intentá de nuevo.")

pedir_temperatura()


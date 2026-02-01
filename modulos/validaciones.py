def pedir_int(mensaje, min_val=None, max_val=None):
    while True:
        texto = input(mensaje).strip()
        try:
            n = int(texto)
        except ValueError:
            print("Entrada inválida. Debes escribir un número entero.")
            continue

        if min_val is not None and n < min_val:
            print(f"Debe ser >= {min_val}.")
            continue
        if max_val is not None and n > max_val:
            print(f"Debe ser <= {max_val}.")
            continue

        return n


def pedir_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("No puede estar vacío.")
            continue
        return texto


def pedir_opcion(mensaje, opciones_validas):
    while True:
        n = pedir_int(mensaje)
        if n in opciones_validas:
            return n
        print(f"Opción inválida. Debe ser una de: {sorted(opciones_validas)}")

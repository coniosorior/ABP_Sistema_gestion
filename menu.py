def mostrar_menu():
    print("\n===== TIENDA DE ALIMENTO PARA MASCOTAS =====")
    print("1) Agregar producto")
    print("2) Listar productos")
    print("3) Buscar / Consultar stock")
    print("4) Movimientos de stock")
    print("5) Salir")


def listar_productos(productos, eliminados):
    while True:
        print("\n--- Lista de productos ---")

        if not productos:
            print("No hay productos registrados.")
        else:
            for producto in productos:
                print(
                    f"ID: {producto['id']} | "
                    f"Nombre: {producto['nombre']} | "
                    f"Precio: ${producto['precio']} | "
                    f"Stock: {producto['stock']} | "
                    f"Mascota: {producto['tipo_mascota']}"
                )

        print("\n--- Productos eliminados ---")
        if not eliminados:
            print("No hay productos eliminados.")
        else:
            for producto in eliminados:
                print(
                    f"ID: {producto['id']} | "
                    f"Nombre: {producto['nombre']} | "
                    f"Precio: ${producto['precio']} | "
                    f"Stock: {producto['stock']} | "
                    f"Mascota: {producto['tipo_mascota']}"
                )

        print("\nOpciones:")
        print("1) Eliminar producto")
        print("2) Volver al menú principal")

        opcion = input("Elige una opción (1-2): ").strip()

        if opcion == "1":
            if not productos:
                print("No hay productos para eliminar.")
            else:
                eliminar_producto(productos, eliminados)
        elif opcion == "2":
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

def eliminar_producto(productos, eliminados):
    id_str = input("Ingresa el ID del producto a eliminar: ").strip()
    try:
        id_eliminar = int(id_str)
    except ValueError:
        print("ID inválido. Debe ser un número entero.")
        return

    for i, producto in enumerate(productos):
        if producto["id"] == id_eliminar:
            producto_eliminado = productos.pop(i)     
            eliminados.append(producto_eliminado)     
            print("Producto eliminado.")
            return

    print("No se encontró un producto con ese ID.")

def agregar_producto(productos, ids_usados):
    print("\n--- Agregar producto ---")

    
    while True:
        id_str = input("ID: ").strip()
        try:
            nuevo_id = int(id_str)
        except ValueError:
            print("ID inválido. Debe ser un número entero.")
            continue

        if nuevo_id <= 0:
            print("ID inválido. Debe ser mayor que 0.")
            continue

        if nuevo_id in ids_usados:
            print("Ese ID ya existe. Ingresa otro.")
            continue

        break  
  
    while True:
        nombre = input("Nombre del producto: ").strip()
        if nombre == "":
            print("Nombre inválido. No puede estar vacío.")
            continue
        break

    while True:
        precio_str = input("Precio (CLP):").strip()
        try:
            precio = int(precio_str)
        except ValueError:
            print("Precio inválido. Debe ser un número entero.")
            continue

        if precio <= 0:
            print("Precio inválido. Debe ser mayor que 0.")
            continue

        break

    while True:
        stock_str = input("Stock (entero >= 0): ").strip()
        try:
            stock = int(stock_str)
        except ValueError:
            print("Stock inválido. Debe ser un número entero.")
            continue

        if stock < 0:
            print("Stock inválido. No puede ser negativo.")
            continue

        break

    while True:
        tipo_mascota = input("Tipo de mascota (perro/gato): ").strip().lower()
        if tipo_mascota not in ("perro", "gato"):
            print("Tipo inválido. Debe ser 'perro' o 'gato'.")
            continue
        break

    nuevo_producto = {
        "id": nuevo_id,
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "tipo_mascota": tipo_mascota
    }

    productos.append(nuevo_producto)
    ids_usados.add(nuevo_id)

    print("\nProducto agregado correctamente:")
    print(
    f"ID: {nuevo_producto['id']} | "
    f"Nombre: {nuevo_producto['nombre']} | "
    f"Precio: ${nuevo_producto['precio']} | "
    f"Stock: {nuevo_producto['stock']} | "
    f"Mascota: {nuevo_producto['tipo_mascota']}"
)

def consultar_stock(productos):
    while True:
        print("\n--- Buscar / Consultar stock ---")
        print("1) Buscar por ID")
        print("2) Volver al menú principal")

        opcion = input("Elige una opción (1-2): ").strip()

        if opcion == "2":
            break
        elif opcion != "1":
            print("Opción inválida. Intenta nuevamente.")
            continue

        id_str = input("Ingresa el ID del producto: ").strip()
        try:
            id_buscar = int(id_str)
        except ValueError:
            print("ID inválido. Debe ser un número entero.")
            continue

        encontrado = False
        for producto in productos:
            if producto["id"] == id_buscar:
                print("\nProducto encontrado:")
                print(
                    f"ID: {producto['id']} | "
                    f"Nombre: {producto['nombre']} | "
                    f"Precio: ${producto['precio']} | "
                    f"Stock: {producto['stock']} | "
                    f"Mascota: {producto['tipo_mascota']}"
                )
                encontrado = True
                break

        if not encontrado:
            print("No se encontró un producto activo con ese ID.")

def movimientos_stock(productos):
    while True:
        print("\n--- Movimientos de stock ---")
        print("1) Entrada de stock (sumar)")
        print("2) Salida de stock (restar / venta)")
        print("3) Volver al menú principal")

        opcion = input("Elige una opción (1-3): ").strip()

        if opcion == "3":
            break
        elif opcion not in ("1", "2"):
            print("Opción inválida. Intenta nuevamente.")
            continue

        # Pedir ID del producto
        id_str = input("Ingresa el ID del producto: ").strip()
        try:
            id_producto = int(id_str)
        except ValueError:
            print("ID inválido. Debe ser un número entero.")
            continue

        # Buscar producto
        producto_encontrado = None
        for producto in productos:
            if producto["id"] == id_producto:
                producto_encontrado = producto
                break

        if producto_encontrado is None:
            print("No se encontró un producto activo con ese ID.")
            continue

        # Pedir cantidad
        cantidad_str = input("Ingresa la cantidad (entero > 0): ").strip()
        try:
            cantidad = int(cantidad_str)
        except ValueError:
            print("Cantidad inválida. Debe ser un número entero.")
            continue

        if cantidad <= 0:
            print("Cantidad inválida. Debe ser mayor que 0.")
            continue

        # Entrada
        if opcion == "1":
            producto_encontrado["stock"] += cantidad
            print("Entrada registrada.")
            print(f"Stock actualizado: {producto_encontrado['stock']}")

        # Salida
        elif opcion == "2":
            if producto_encontrado["stock"] < cantidad:
                print("Stock insuficiente. No se puede realizar la salida.")
                print(f"Stock actual: {producto_encontrado['stock']}")
                continue

            producto_encontrado["stock"] -= cantidad
            print("Salida registrada.")
            print(f"Stock actualizado: {producto_encontrado['stock']}")


def pedir_opcion_menu():
    while True:
        opcion_str = input("Elige una opción (1-5): ").strip()

        try:
            opcion = int(opcion_str)
        except ValueError:
            print("Opción inválida. Debes escribir un número del 1 al 5. Intenta nuevamente.")
            continue

        if 1 <= opcion <= 5:
            return opcion
        else:
            print("Opción inválida. Debes escoger un número del 1 al 5. Intenta nuevamente.")


def main():
    productos = [
        {"id": 1, "nombre": "Alimento perro adulto 10kg", "precio": 25990, "stock": 12, "tipo_mascota": "perro"},
        {"id": 2, "nombre": "Alimento gato salmón 3kg", "precio": 18990, "stock": 5, "tipo_mascota": "gato"},
        {"id": 3, "nombre": "Snack dental perro 200g", "precio": 4990, "stock": 20, "tipo_mascota": "perro"},
        {"id": 4, "nombre": "Alimento cachorro 8kg", "precio": 23990, "stock": 7, "tipo_mascota": "perro"},
        {"id": 5, "nombre": "Arena sanitaria gato 10L", "precio": 9990, "stock": 15, "tipo_mascota": "gato"},
    ]

    eliminados = []

    ids_usados = {p["id"] for p in productos}

    while True:
        mostrar_menu()
        opcion = pedir_opcion_menu()

        if opcion == 1:
            agregar_producto(productos, ids_usados)
        elif opcion == 2:
            listar_productos(productos, eliminados)
        elif opcion == 3:
            consultar_stock(productos)
        elif opcion == 4:
            movimientos_stock(productos)
        elif opcion == 5:
            print("Saliendo del sistema... ¡Hasta luego!")
            break


if __name__ == "__main__":
    main()


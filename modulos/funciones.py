from validaciones import pedir_int, pedir_texto_no_vacio, pedir_opcion


def login(usuarios):
    print("\n===== LOGIN =====")
    while True:
        user_in = input("Usuario: ").strip()
        pass_in = input("Contraseña: ").strip()

        for u in usuarios:
            if u.get("user") == user_in and u.get("pass") == pass_in:
                print(f"\nBienvenido, {u.get('user')} (Rol: {u.get('rol')})")
                return u

        print("Usuario o contraseña incorrectos. Intenta nuevamente.")


def mostrar_menu():
    print("\n===== TIENDA DE ALIMENTO PARA MASCOTAS =====")
    print("1) Agregar producto")
    print("2) Listar productos")
    print("3) Buscar / Consultar stock")
    print("4) Movimientos de stock")
    print("5) Salir")


def pedir_opcion_menu():
    return pedir_opcion("Elige una opción (1-5): ", {1, 2, 3, 4, 5})


def tiene_permiso(rol, opcion_menu):
    if opcion_menu == 5:
        return True

    if rol == "Admin":
        return True

    if rol == "Usuario":
        return opcion_menu in (2, 3, 4)

    if rol == "Invitado":
        return opcion_menu == 3

    return False


def listar_productos(productos, eliminados, rol):
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

        opcion = pedir_opcion("Elige una opción (1-2): ", {1, 2})

        if opcion == 1:
            if rol != "Admin":
                print("Tu rol no tiene permiso para eliminar productos.")
                continue

            if not productos:
                print("No hay productos para eliminar.")
            else:
                eliminar_producto(productos, eliminados)

        else:  # opcion == 2
            break


def eliminar_producto(productos, eliminados):
    id_eliminar = pedir_int("Ingresa el ID del producto a eliminar: ", min_val=1)

    for producto in productos:
        if producto["id"] == id_eliminar:
            productos.remove(producto)      # .remove()
            eliminados.append(producto)     # .append()
            print("Producto eliminado.")
            return

    print("No se encontró un producto con ese ID.")


def agregar_producto(productos, ids_usados):
    print("\n--- Agregar producto ---")

    while True:
        nuevo_id = pedir_int("ID: ", min_val=1)
        if nuevo_id in ids_usados:
            print("Ese ID ya existe. Ingresa otro.")
            continue
        break

    nombre = pedir_texto_no_vacio("Nombre del producto: ")
    precio = pedir_int("Precio (CLP): ", min_val=1)
    stock = pedir_int("Stock (entero >= 0): ", min_val=0)

    while True:
        tipo_mascota = input("Tipo de mascota (perro/gato): ").strip().lower()
        if tipo_mascota in ("perro", "gato"):
            break
        print("Tipo inválido. Debe ser 'perro' o 'gato'.")

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

        opcion = pedir_opcion("Elige una opción (1-2): ", {1, 2})
        if opcion == 2:
            break

        id_buscar = pedir_int("Ingresa el ID del producto: ", min_val=1)

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
                break
        else:
            print("No se encontró un producto activo con ese ID.")


def movimientos_stock(productos):
    while True:
        print("\n--- Movimientos de stock ---")
        print("1) Entrada de stock (sumar)")
        print("2) Salida de stock (restar / venta)")
        print("3) Volver al menú principal")

        opcion = pedir_opcion("Elige una opción (1-3): ", {1, 2, 3})
        if opcion == 3:
            break

        id_producto = pedir_int("Ingresa el ID del producto: ", min_val=1)

        producto_encontrado = None
        for producto in productos:
            if producto["id"] == id_producto:
                producto_encontrado = producto
                break

        if producto_encontrado is None:
            print("No se encontró un producto activo con ese ID.")
            continue

        cantidad = pedir_int("Ingresa la cantidad (entero > 0): ", min_val=1)

        if opcion == 1:
            producto_encontrado["stock"] += cantidad
            print("Entrada registrada.")
            print(f"Stock actualizado: {producto_encontrado['stock']}")
        else:
            if producto_encontrado["stock"] < cantidad:
                print("Stock insuficiente. No se puede realizar la salida.")
                print(f"Stock actual: {producto_encontrado['stock']}")
                continue

            producto_encontrado["stock"] -= cantidad
            print("Salida registrada.")
            print(f"Stock actualizado: {producto_encontrado['stock']}")

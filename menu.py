from modulos.funciones import (login, mostrar_menu, pedir_opcion_menu, tiene_permiso,
    agregar_producto, listar_productos, consultar_stock, movimientos_stock)

ROLES = ("Admin", "Usuario", "Invitado")

usuarios = [
    {"user": "admin", "pass": "1234", "rol": "Admin"},
    {"user": "usuario", "pass": "1234", "rol": "Usuario"},
    {"user": "invitado", "pass": "1234", "rol": "Invitado"},
]

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

    usuario_actual = login(usuarios)
    rol_actual = usuario_actual.get("rol")

    while True:
        mostrar_menu()
        opcion = pedir_opcion_menu()

        if not tiene_permiso(rol_actual, opcion):
            print("Acceso denegado: tu rol no tiene permiso para esa opción.")
            continue

        if opcion == 1:
            agregar_producto(productos, ids_usados)
        elif opcion == 2:
            listar_productos(productos, eliminados, rol_actual)
        elif opcion == 3:
            consultar_stock(productos)
        elif opcion == 4:
            movimientos_stock(productos)
        elif opcion == 5:
            print("Saliendo del sistema... ¡Hasta luego!")
            break


if __name__ == "__main__":
    main()

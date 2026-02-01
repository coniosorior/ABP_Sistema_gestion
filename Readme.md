# Sistema de Gestión para Tienda de Alimentos para Mascotas

## 1. Descripción General del Sistema

Este proyecto corresponde a un **sistema de gestión para una tienda de alimentos para mascotas, especificamente perros y gatos**,  
El sistema permite administrar productos, controlar el stock disponible y gestionar el acceso a las funcionalidades según distintos **roles de usuario**.

El sistema opera mediante un menú en consola y está diseñado para apoyar las tareas básicas de administración interna de una tienda, asegurando orden, control y validación de la información ingresada.

---

## 2. Objetivo del Sistema

El objetivo principal del sistema es:

- Gestionar el inventario de productos de una tienda de mascotas.
- Controlar entradas y salidas de stock.
- Permitir la consulta de productos por ID.
- Restringir el acceso a las funcionalidades según el rol del usuario.

El sistema se enfoca en el **control de inventario y operaciones internas**, sin incluir procesos de venta ni persistencia en bases de datos externas.

---

## 3. Roles de Usuario y Permisos

El sistema define tres roles de usuario, cada uno con distintos niveles de acceso:

- **Administrador (Admin)**  
  Acceso total al sistema. Puede: agregar productos, listar productos, eliminar productos, consultar stock y realizar movimientos de stock.

- **Usuario**  
  Puede listar productos, eliminar productos, consultar stock y realizar movimientos de stock. No tiene permisos para agregar.

- **Invitado**  
  Acceso restringido. Solo puede consultar el stock de los productos.

El control de permisos se gestiona mediante validaciones antes de ejecutar cada opción del menú.

---

## 4. Funcionalidades Implementadas

El sistema incluye las siguientes funcionalidades:

- **Inicio de sesión** con validación de usuario y rol.
- **Gestión de productos**:
  - Agregar nuevos productos.
  - Listar productos activos.
  - Eliminar productos (los productos eliminados se almacenan en una lista separada).
- **Consulta de stock** por ID de producto.
- **Movimientos de stock**:
  - Entrada de stock.
  - Salida de stock (venta).
- **Validación de datos** para evitar errores de ingreso.
- **Control de acceso** según el rol del usuario.

---

## 5. Estructuras de Datos Utilizadas

El sistema utiliza distintas estructuras de datos de Python para organizar la información:

- **Listas (`list`)**  
  Se utilizan para almacenar productos, usuarios y productos eliminados.

- **Diccionarios (`dict`)**  
  Representan entidades como productos y usuarios, permitiendo un acceso claro a sus atributos.

- **Tuplas (`tuple`)**  
  Definen los roles del sistema como datos inmutables.

- **Conjuntos (`set`)**  
  Se utilizan para evitar duplicación de identificadores (IDs de productos).

Estas estructuras permiten un manejo eficiente y ordenado de la información.

---

## 6. Organización del Proyecto (Modularización)

El proyecto está organizado en módulos para mejorar la claridad, reutilización y mantenimiento del código:

- **main.py**  
  Controla el flujo principal del programa y la interacción entre los módulos.

- **funciones.py**  
  Contiene la lógica del sistema: menús, gestión de productos, control de stock y permisos.

- **validaciones.py**  
  Centraliza las validaciones de entrada de datos para asegurar que la información ingresada sea correcta.

---

## 7. Análisis del Proceso de Desarrollo

El desarrollo del sistema se realizó siguiendo una secuencia lógica:

1. Se muestra sistema en donde se indetifica el menu principal del Sistema de gestion y funcionalidades necesarias.
2. Implementación de la lógica principal del sistema.
3. Se crea el archivo funciones que contiene las funciones principales del sistema, encargadas de realizar las operaciones como agregar productos, listar información, consultar stock y gestionar movimientos.
4. Separación del código en módulos para reducir duplicación.
5. Aplicación de validaciones para evitar erroes en el uso del sistema de gestión.
6. Implementación de control de acceso mediante roles.
7. Dentro de la carpeta de **Abp3** se incluyen imagenes para la demostración y validación del desarrollo del Sistema de gestión para mascotas.

---

## 9. Consideraciones Finales

El sistema está enfocado para la gestión básica de productos y stock para una tienda de mascotas, aplicando validaciones, modularización y control de permisos.


## 10. Instrucciones de ejecución

Para ejecutar correctamente el sistema de gestión, siga los pasos a continuación:

1. Una vez clonado el repositorio desde GitHub utilizando el enlace:  
   https://github.com/coniosorior/ABP_Sistema_gestion.git

2. Acceder a Python y abrir la carpeta del proyecto denominada **Abp3**.

3. Para ejecutar el sistema de gestión, ejecutar el archivo principal **menu.py** 


4. Al iniciar el programa, el sistema solicitará credenciales de acceso (usuario y contraseña).
   Dependiendo del rol, las opciones disponibles en el menú variarán según los permisos asignados.

**Credenciales disponibles por rol**

__Administrador__

Usuario: admin
Contraseña: 1234

__Usuario__

Usuario: usuario
Contraseña: 1234

__Invitado__

Usuario: invitado
Contraseña: 1234


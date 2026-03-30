# Sistema de Gestión de Inventario en Python

## Descripción

Este proyecto es un **sistema de gestión de estudiantes en consola**
desarrollado en Python.\
Permite administrar estudiantes mediante un menú interactivo que facilita
operaciones básicas como:

-   Agregar estudiantes
-   Mostrarlos
-   Buscar estudiantes
-   Actualizar información
-   Eliminar estudiantes

El sistema utiliza **listas, diccionarios, funciones y manejo de errores** para crear una pequeña aplicación funcional de
gestión de datos.

------------------------------------------------------------------------

# Características principales

## Gestión de productos

El programa permite:

-   Añadir estudiantes con **nombre, edad, programa y estado**
-   Mostrar todos los estudiantes en formato de tabla
-   Buscar estudiantes por nombre o id
-   Actualizar cualquier dato del estudiante
-   Eliminar estudiantes del sistema

------------------------------------------------------------------------

# Estructura del proyecto

El proyecto está organizado en módulos para mantener el código limpio y
reutilizable.

    project/
    │
    ├── main.py          # Programa principal con el menú interactivo
    ├── functions.py     # Funciones para manipular el inventario
    └── README.md        # Documentación del proyecto

------------------------------------------------------------------------

# Requisitos

-   Python **3.8 o superior**

No se requieren librerías externas.

------------------------------------------------------------------------

# Cómo ejecutar el programa

1.  Clona o descarga el proyecto.
2.  Abre una terminal en la carpeta del proyecto.
3.  Ejecuta:

``` bash
python main.py
```

------------------------------------------------------------------------

# Menú del sistema

Al ejecutar el programa aparecerá el siguiente menú:

           Hi!, Welcome.
¿what do you like to do today?
    1. Add student.
    2. Show student list.
    3. Search student.
    4. Update student.
    5. Remove student.
    0. Exit

Cada opción permite realizar una acción específica sobre los estudiantes.

------------------------------------------------------------------------

# Manejo de errores

El programa incluye validación para:

-   Valores negativos
-   Entradas incorrectas del usuario

Esto evita que el programa se cierre inesperadamente.

------------------------------------------------------------------------

# Conceptos de Python utilizados

Este proyecto demuestra el uso de:

-   Funciones
-   Listas y diccionarios
-   Expresiones lambda
-   Generadores
-   Manejo de errores (`try / except`)
-   Organización modular del código

------------------------------------------------------------------------

# Posibles mejoras futuras

Algunas mejoras que se podrían implementar:

-   Interfaz gráfica (Tkinter o PyQt)
-   Base de datos (SQLite o MySQL)
-   Control de usuarios
-   Historial de movimientos de inventario
-   Exportación a Excel

------------------------------------------------------------------------

# Autor

Riwi
**Dylan Gamero**.
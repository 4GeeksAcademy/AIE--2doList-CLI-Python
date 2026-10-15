# Gestor de tareas CLI en Python

Aplicación ligera de terminal para registrar y consultar tareas pendientes. Está pensada para que un equipo pueda mantener una lista sencilla entre turnos y guardar su progreso en un archivo local.

## Funcionalidades

- Agregar tantas tareas como se necesiten durante una sesión.
- Mostrar las tareas pendientes con posiciones numeradas desde 1.
- Eliminar una tarea indicando su posición.
- Guardar la lista en `todos.csv` y cargarla en otra ejecución.
- Usar únicamente la biblioteca estándar de Python; no requiere instalar paquetes.

## Requisitos

- Python 3 instalado.
- Una terminal o línea de comandos.

## Estructura del proyecto

```text
.
├── main.py          # Aplicación de terminal
├── README.md        # Guía del proyecto
├── Promptinicial.md # Requisitos originales
├── Explicacion.md   # Explicación del código para principiantes
└── todos.csv        # Datos guardados; se crea al guardar por primera vez
```

`todos.csv` es un archivo de datos local, no código fuente. Puede no existir antes del primer guardado.

## Ejecutar

Desde la carpeta del proyecto, ejecuta:

```bash
python3 main.py
```

En algunos sistemas, el comando disponible puede ser `python main.py`.

Al iniciar, la aplicación intenta cargar `todos.csv`. Si el archivo no existe, comienza con una lista vacía. Después muestra este menú:

```text
1. Agregar tarea  2. Mostrar tareas  3. Eliminar tarea
4. Guardar  5. Cargar  0. Salir
```

### Ejemplo de uso

1. Elige `1` y escribe el título de la tarea.
2. Elige `2` para ver la lista y sus posiciones.
3. Elige `3` y escribe la posición para eliminar una tarea.
4. Elige `4` para guardar los cambios en `todos.csv`.
5. Elige `0` para salir.

**Importante:** salir no guarda automáticamente. Guarda con la opción `4` antes de cerrar la aplicación para conservar los cambios. La opción `5` vuelve a cargar el archivo y reemplaza la lista que esté en memoria; guarda primero si necesitas conservar esos cambios.

## Funciones principales

| Función | Descripción |
| --- | --- |
| `add_one_task(title)` | Limpia el título y agrega la tarea a la lista en memoria. |
| `print_list()` | Muestra las tareas con posiciones desde 1, o avisa si no hay tareas. |
| `delete_task(number_to_delete)` | Elimina la tarea que ocupa la posición indicada y valida que exista. |
| `save_todos()` | Escribe las tareas actuales en `todos.csv`, reemplazando su contenido anterior. |
| `load_todos()` | Carga las tareas de `todos.csv` y reemplaza la lista en memoria. |
| `main()` | Controla el menú y conecta las opciones con las funciones anteriores. |

## Archivo de datos

Las tareas se guardan en formato CSV, una tarea por fila, usando UTF-8. El módulo estándar `csv` se encarga de guardar títulos que contengan comas correctamente. El archivo se busca en el directorio actual desde el que se ejecuta el comando.

## Alcance

En esta versión no se editan tareas: para cambiar un título, elimina la tarea y vuelve a crearla. Las tareas nuevas solo están en memoria hasta que se usa la opción para guardar.

Para conocer el código con más detalle, consulta [Explicacion.md](Explicacion.md).
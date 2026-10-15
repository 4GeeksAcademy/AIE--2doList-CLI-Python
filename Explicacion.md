# Explicación de la herramienta

Este documento explica `main.py` paso a paso, suponiendo que estás empezando a programar. No necesitas conocer Python de antemano: cada idea aparece junto a la parte del programa donde se usa.

## La idea general

La aplicación mantiene las tareas en una lista de Python mientras está abierta. Puedes agregar, mostrar o eliminar tareas desde el menú. Para conservarlas después de cerrar la terminal, el programa puede escribirlas en `todos.csv` y leerlas de nuevo más adelante.

Hay dos lugares donde pueden estar las tareas:

- **Memoria:** la lista `TASKS` que el programa usa durante la ejecución. Desaparece al cerrar el programa.
- **Archivo:** `todos.csv`, que permanece guardado en el disco hasta que se modifica o elimina.

La opción **Guardar** copia la lista de memoria al archivo. La opción **Cargar** hace lo contrario y reemplaza la lista de memoria con el contenido del archivo.

## Preparar el programa

```python
import csv

TASKS = []
TODO_FILE = "todos.csv"
```

- `import csv` carga una herramienta que ya viene con Python para leer y escribir archivos CSV. No hay que instalarla.
- `TASKS = []` crea una lista vacía. Una lista puede guardar varios valores; aquí cada valor es el título de una tarea.
- `TODO_FILE` guarda el nombre del archivo. Usar una constante evita repetir el texto `todos.csv` por todo el programa.

## `add_one_task(title)`

Esta función agrega una tarea a la lista:

1. `title` es un **parámetro**: el dato que recibe la función, en este caso el título escrito por la persona.
2. `title.strip()` quita espacios al principio y al final. Por ejemplo, convierte `"  Revisar ruta  "` en `"Revisar ruta"`.
3. `if not title` comprueba si el título quedó vacío. Si lo está, muestra un mensaje y `return` termina la función sin agregar nada.
4. `TASKS.append(title)` agrega el título al final de la lista.

Cada vez que eliges agregar una tarea, el menú vuelve a aparecer, así que puedes repetir este proceso tantas veces como necesites.

## `print_list()`

Esta función muestra las tareas:

- Primero comprueba si `TASKS` está vacía. Si no hay elementos, muestra un mensaje y termina.
- `enumerate(TASKS, start=1)` recorre la lista y entrega dos datos: la posición y el título. `start=1` hace que las posiciones visibles comiencen en 1.
- `for position, title in ...` repite el bloque para cada tarea.
- `print(f"{position}. {title}")` muestra ambos datos. La letra `f` permite insertar variables dentro del texto entre llaves.

Las personas suelen contar desde 1, pero Python cuenta las posiciones internas de una lista desde 0. Por eso esta función muestra posiciones para las personas y `delete_task()` las adapta al índice que Python necesita.

## `delete_task(number_to_delete)`

Esta función elimina una tarea según la posición que escribe la persona:

1. Comprueba que el número sea al menos 1 y no supere `len(TASKS)`. `len(...)` indica cuántos elementos hay en la lista.
2. Si el número no corresponde a una tarea, muestra un aviso y no cambia la lista.
3. `TASKS.pop(number_to_delete - 1)` elimina y devuelve un elemento de la lista. Se resta 1 porque, por ejemplo, la tarea visible como número 1 está en el índice interno 0 de Python.

## `save_todos()`

Esta función guarda las tareas en el archivo:

- `open(...)` abre el archivo. El modo `"w"` significa escribir y reemplazar el contenido anterior.
- `encoding="utf-8"` permite guardar correctamente letras como `ñ` y vocales con tilde.
- `newline=""` es una opción recomendada por el módulo `csv` para controlar correctamente los saltos de línea.
- `with` cierra el archivo automáticamente al terminar el bloque, incluso si ocurre un error.
- `csv.writer(todos_file)` crea una herramienta para escribir filas CSV.
- `writer.writerows(...)` escribe una fila por cada tarea.

Por ejemplo, la tarea `"Revisar carga"` queda en una fila del archivo. El módulo `csv` también protege títulos que contienen comas para que no se interpreten como varias columnas.

## `load_todos()`

Esta función carga las tareas guardadas:

- Abre `todos.csv` en modo de lectura y crea un lector con `csv.reader`.
- Cada `row` representa una fila del archivo. El programa toma `row[0]`, es decir, el primer campo de esa fila.
- La condición `if row and row[0]` evita usar filas vacías.
- `TASKS[:] = ...` reemplaza el contenido de la lista actual con las tareas leídas. Esto significa que cargar no añade las tareas al final: sustituye la lista en memoria.
- `try` y `except FileNotFoundError` manejan el caso en que todavía no existe el archivo. Al iniciar sin un archivo guardado, el programa empieza con la lista vacía.

Como **Cargar** reemplaza la lista actual, guarda primero si tienes tareas nuevas que aún no estén en el archivo.

## `main()` y el menú

`main()` coordina la aplicación:

1. Llama a `load_todos()` al iniciar para recuperar el trabajo guardado.
2. `while True` mantiene el menú abierto y permite realizar varias operaciones en la misma ejecución.
3. `input(...)` muestra una pregunta y espera a que escribas una respuesta. El resultado es texto.
4. Las comparaciones `choice == "1"`, `choice == "2"`, etc., deciden qué acción ejecutar según la opción elegida.
5. Para borrar, `int(...)` convierte la respuesta de texto a un número entero. Si no se puede convertir, `except ValueError` muestra un mensaje en vez de cerrar la aplicación.
6. La opción `0` ejecuta `break`, que sale del bucle y termina el menú.

La opción `4` guarda y la opción `5` vuelve a cargar. Salir con `0` no guarda automáticamente.

## Inicio del archivo

```python
if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nHasta luego.")
```

Python asigna el valor `"__main__"` a `__name__` cuando ejecutas el archivo directamente, por ejemplo con `python3 main.py`. Esa condición inicia el menú solo en ese caso.

El bloque `try` permite detectar dos formas de interrupción: `EOFError` cuando la entrada termina inesperadamente y `KeyboardInterrupt` cuando se pulsa `Ctrl+C`. En ambos casos, el programa muestra un mensaje de salida.

## Resumen del recorrido

```text
Iniciar programa
    -> cargar todos.csv si existe
    -> mostrar menú repetidamente
    -> cambiar tareas en memoria
    -> guardar explícitamente cuando se elige la opción 4
```

Recuerda: si agregas o eliminas tareas y quieres conservar el resultado, elige **Guardar** antes de salir.
# Prompt inicial: Lista de tareas CLI en Python

Quiero que actúes como programador sénior experto en Python y crees una herramienta ligera de terminal para que cualquier persona pueda gestionar tareas rápidamente desde la línea de comandos. Usa como contexto el siguiente escenario:

## Escenario

Te has unido al equipo de herramientas internas de una empresa pequeña de logística. Hoy, los coordinadores operativos anotan tareas pendientes entre mensajes de chat y notas sueltas, y eso provoca que se pierdan seguimientos importantes entre turnos. Tu product manager te ha pedido una herramienta ligera de terminal para que cualquier persona pueda gestionar tareas rápidamente desde la línea de comandos.

La aplicación debe permitir registrar nuevas tareas cuando llegan, consultar toda la lista en cualquier momento y eliminar tareas completadas indicando su posición numérica. Como el equipo cierra y abre terminales durante el día, también necesita guardar tareas en un archivo local y volver a cargarlas después sin perder progreso.

## Comportamiento requerido

- Agregar una nueva tarea por título.
- Mostrar todas las tareas pendientes con su posición numérica.
- Eliminar una tarea por su posición en la lista.
- Guardar tareas en un archivo `todos.csv`.
- Cargar nuevamente las tareas desde `todos.csv`.

No hace falta editar tareas en esta versión; el flujo esperado es eliminar y volver a crear.

## Requisitos esenciales

Es de **VITAL IMPORTANCIA** que la aplicación cumpla con lo siguiente:

- Implementar `add_one_task(title)` para agregar una nueva tarea a la lista en memoria.
- Implementar `print_list()` para mostrar todas las tareas con posiciones numéricas claras.
- Implementar `delete_task(number_to_delete)` para eliminar una tarea usando su posición.
- Implementar `save_todos()` para persistir las tareas en `todos.csv`.
- Implementar `load_todos()` para cargar tareas desde `todos.csv` hacia la memoria.
- Asegurar que el usuario pueda agregar tantas tareas como necesite en la misma ejecución.
- Asegurar que toda la experiencia funcione desde la línea de comandos y coincida con la referencia visual.

## Restricción técnica

**IMPORTANTE:** En esta versión del proyecto usa solo herramientas de la biblioteca estándar de Python para la entrada y salida de archivos y el manejo de la CLI.

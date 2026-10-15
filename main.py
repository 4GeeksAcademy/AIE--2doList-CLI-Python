import csv


TASKS = []
TODO_FILE = "todos.csv"


def add_one_task(title):
    title = title.strip()
    if not title:
        print("El título no puede estar vacío.")
        return
    TASKS.append(title)
    print("Tarea agregada.")


def print_list():
    if not TASKS:
        print("No hay tareas pendientes.")
        return
    for position, title in enumerate(TASKS, start=1):
        print(f"{position}. {title}")


def delete_task(number_to_delete):
    if number_to_delete < 1 or number_to_delete > len(TASKS):
        print("Esa posición no existe.")
        return
    deleted_task = TASKS.pop(number_to_delete - 1)
    print(f'Tarea eliminada: "{deleted_task}"')


def save_todos():
    with open(TODO_FILE, "w", newline="", encoding="utf-8") as todos_file:
        writer = csv.writer(todos_file)
        writer.writerows([task] for task in TASKS)
    print(f"Tareas guardadas en {TODO_FILE}.")


def load_todos():
    try:
        with open(TODO_FILE, newline="", encoding="utf-8") as todos_file:
            TASKS[:] = [row[0] for row in csv.reader(todos_file) if row and row[0]]
    except FileNotFoundError:
        TASKS.clear()


def main():
    load_todos()
    print("Lista de tareas")

    while True:
        print("\n1. Agregar tarea  2. Mostrar tareas  3. Eliminar tarea")
        print("4. Guardar  5. Cargar  0. Salir")
        choice = input("Elige una opción: ").strip()

        if choice == "1":
            add_one_task(input("Título de la tarea: "))
        elif choice == "2":
            print_list()
        elif choice == "3":
            try:
                number_to_delete = int(input("Número de la tarea que quieres eliminar: "))
                delete_task(number_to_delete)
            except ValueError:
                print("Introduce un número válido.")
        elif choice == "4":
            save_todos()
        elif choice == "5":
            load_todos()
            print("Tareas cargadas.")
        elif choice == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nHasta luego.")
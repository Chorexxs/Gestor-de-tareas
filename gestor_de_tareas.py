tasks = []
completed_tasks = []
categories = {}

# Función para agregar tarea con prioridad y fecha de vencimiento
def add_task():
    task = input("Ingresa la tarea que deseas agregar: ")
    priority = input("Ingresa la prioridad de la tarea (alta, media, baja): ")
    due_date = input("Ingresa la fecha de vencimiento (opcional): ")
    category = input("Ingresa la categoría de la tarea (opcional): ")

    if due_date:
        task_info = (task, priority, due_date, category)
    else:
        task_info = (task, priority, category) if category else (task, priority)
    
    tasks.append(task_info)
    if category:
        categories.setdefault(category, []).append(task_info)
    print(f"Tarea '{task}' agregada con éxito.")

# Función para mostrar tareas
def show_tasks():
    print("\n------ Tareas ------")
    if len(tasks) == 0:
        print("No hay tareas pendientes.")
    else:
        for i, task_info in enumerate(tasks, 1):
            task, priority, due_date, category = task_info
            if due_date:
                print(f"{i}. {task} - Prioridad: {priority}, Vencimiento: {due_date}, Categoría: {category}")
            else:
                print(f"{i}. {task} - Prioridad: {priority}, Categoría: {category}")

# Función para editar tarea
def edit_task():
    show_tasks()
    task_index = int(input("Ingresa el número de tarea que deseas editar: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("Número de tarea inválido.")
    else:
        task_info = tasks[task_index]
        task, priority, due_date, category = task_info

        new_task = input("Ingresa la nueva tarea: ")
        new_priority = input("Ingresa la nueva prioridad (alta, media, baja): ")
        new_due_date = input("Ingresa la nueva fecha de vencimiento (opcional): ")
        new_category = input("Ingresa la nueva categoría de la tarea (opcional): ")

        if new_due_date:
            updated_task_info = (new_task, new_priority, new_due_date, new_category)
        else:
            updated_task_info = (new_task, new_priority, new_category) if new_category else (new_task, new_priority)
        
        tasks[task_index] = updated_task_info
        if category:
            categories[category].remove(task_info)
        if new_category:
            categories.setdefault(new_category, []).append(updated_task_info)
        print("Tarea actualizada con éxito.")

# Función para eliminar tarea
def delete_task():
    show_tasks()
    task_index = int(input("Ingresa el número de tarea que deseas eliminar: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("Número de tarea inválido.")
    else:
        deleted_task_info = tasks.pop(task_index)
        deleted_task, _, _, category = deleted_task_info
        if category:
            categories[category].remove(deleted_task_info)
        print(f"Tarea '{deleted_task}' eliminada con éxito.")

# Función para filtrar tareas por prioridad
def filter_by_priority():
    priority_filter = input("Ingresa la prioridad para filtrar (alta, media, baja): ")
    filtered_tasks = [task_info for task_info in tasks if len(task_info) == 3 and task_info[1] == priority_filter]
    show_filtered_tasks(filtered_tasks)

# Función para filtrar tareas por fecha de vencimiento
def filter_by_due_date():
    due_date_filter = input("Ingresa la fecha de vencimiento para filtrar (opcional): ")
    filtered_tasks = [task_info for task_info in tasks if len(task_info) == 4 and task_info[2] == due_date_filter]
    show_filtered_tasks(filtered_tasks)

# Función para mostrar tareas filtradas
def show_filtered_tasks(filtered_tasks):
    print("\n------ Tareas Filtradas ------")
    if len(filtered_tasks) == 0:
        print("No hay tareas que coincidan con el filtro.")
    else:
        for i, task_info in enumerate(filtered_tasks, 1):
            task, priority, due_date, category = task_info
            if due_date:
                print(f"{i}. {task} - Prioridad: {priority}, Vencimiento: {due_date}, Categoría: {category}")
            else:
                print(f"{i}. {task} - Prioridad: {priority}, Categoría: {category}")

# Función para marcar tarea como completada
def mark_completed():
    show_tasks()
    task_index = int(input("Ingresa el número de tarea completada: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("Número de tarea inválido.")
    else:
        completed_task_info = tasks.pop(task_index)
        completed_task, _, _, category = completed_task_info
        completed_tasks.append(completed_task_info)
        if category:
            categories[category].remove(completed_task_info)
        print(f"Tarea '{completed_task}' marcada como completada.")

# Función para mostrar tareas completadas
def show_completed_tasks():
    print("\n------ Tareas Completadas ------")
    if len(completed_tasks) == 0:
        print("No hay tareas completadas.")
    else:
        for i, completed_task_info in enumerate(completed_tasks, 1):
            completed_task, _, _, category = completed_task_info
            print(f"{i}. {completed_task} - Categoría: {category}")

# Menú principal
while True:
    print("\n------ Gestión de Tareas ------")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Editar tarea")
    print("4. Eliminar tarea")
    print("5. Filtrar por prioridad")
    print("6. Filtrar por fecha de vencimiento")
    print("7. Marcar tarea como completada")
    print("8. Mostrar tareas completadas")
    print("9. Salir")

    option = int(input("Ingresa el número de opción: "))
    
    if option == 1:
        add_task()
    elif option == 2:
        show_tasks()
    elif option == 3:
        edit_task()
    elif option == 4:
        delete_task()
    elif option == 5:
        filter_by_priority()
    elif option == 6:
        filter_by_due_date()
    elif option == 7:
        mark_completed()
    elif option == 8:
        show_completed_tasks()
    elif option == 9:
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida.")

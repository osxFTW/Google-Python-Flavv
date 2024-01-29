categorii = {"curs", "cumparaturi", "munca", "cadouri"}
with open("./categorii.txt", "w") as f:
    for categorie in categorii:
        f.write(categorie + "\n")

categorii_citite = []

with open("./categorii.txt", "r") as f:
    for line in f.readlines():
        categorii_citite.append(line.strip())

def nume_gasit():
    gasit = True
    while gasit:
        nume_task = input("Introduceti numele task-ului:")
        with open("tasks.txt", 'r') as file:
            tasks_citite = []
            for line in file.readlines():
                tasks_citite.append(line.strip().split(","))
            for task in tasks_citite:
                if nume_task in task:
                    print("Task-ul exista deja!")
                    break
                else:
                    gasit = False

def adauga_task():
    flag = True
    while flag:
        gasit = True
        while gasit:
            nume_task = input("Introduceti numele task-ului:")
            with open("tasks.txt", 'r') as file:
                tasks_citite = []
                for line in file.readlines():
                    tasks_citite.append(line.strip().split(","))
                for task in tasks_citite:
                    if nume_task in task:
                        print("Task-ul exista deja!")
                        break
                    else:
                        gasit = False
        dl = input("Introduceti deadline-ul: ")
        persoana = input("Introduceti persoana pentru realizarea task-ului: ")

        while True:
            categorie_task = input("Introduceti categoria task-ului: ")
            if categorie_task in categorii_citite:
                break
            else:
                print("Categoria nu exista")

        with open("tasks.txt", "a") as file:
            file.write(f"{nume_task},{dl},{persoana},{categorie_task}\n")

        while True:
            raspuns = input("Doriti sa continuati? Da/Nu: ")
            if raspuns.lower() == "nu":
                flag = False
                break
            elif raspuns.lower() == "da":
                break
            else:
                print("Raspunsul nu este valid")
                continue

def afisare_dupa_categorie():
    with open("tasks.txt", "r") as f:
        lista_taskuri = []
        for line in f.readlines():
            lista_taskuri.append(line.strip().split(","))
        lista_taskuri.sort(key=lambda x: x[3])
        for task in lista_taskuri:
            print(task)

def delete_line_by_task(task_to_delete):
    with open('tasks.txt', 'r') as file:
        lines = file.readlines()

    # Verificam daca este gasit task ul
    task_gasit = False
    updated_lines = []
    for line in lines:
        if line.strip().split(',')[0] == task_to_delete:
            task_gasit = True
        else:
            updated_lines.append(line)

    # Scriem lista modificata
    with open('tasks.txt', 'w') as file:
        file.writelines(updated_lines)

    if task_gasit:
        print(f'Task-ul "{task_to_delete}" a fost sters.')
    else:
        print(f'Task-ul "{task_to_delete}" nu a fost gasit.')

delete_line_by_task('tasks.txt', 'asd')

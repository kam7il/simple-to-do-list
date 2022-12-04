u_choice = -2
tasks = []


def show_tasks():
    index_task = 0
    for task in tasks:
        print("[" + str(index_task) + "] " + task)
        index_task += 1


def add_task():
    task = input("Wpisz treść zadania które chcesz dodać: ")
    tasks.append(task)
    print("Dodano zadanie")


def delete_task():
    index_task = int(input("Podaj numer zadania do usunięcia: "))

    if index_task < 0 or index_task > len(tasks) - 1:
        print("Zadanie o podanym numerze nie instnieje")
        return

    tasks.pop(index_task)
    print("Usunięto zadanie")


def save_task_file():
    file = open("to_do_list.txt", "w")

    for task in tasks:
        file.write((task + "\n"))
    file.close()


def load_task_file():
    try:
        file = open("to_do_list.txt")

        for line in file.readlines():
            tasks.append(line.strip())

        file.close()
    except FileNotFoundError:
        return


load_task_file()
show_tasks()

while u_choice != 5:

    if u_choice == 1:
        show_tasks()

    if u_choice == 2:
        add_task()

    if u_choice == 3:
        delete_task()

    if u_choice == 4:
        save_task_file()

    print("----------------")
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Zapisz zmiany do pliku")
    print("5. Wyjdź")

    u_choice = int(input("Wybierz liczbę: "))
    print()

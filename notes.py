import json
import datetime


def open_file():
    try:
        with open("notes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


notes = open_file()


def save_file(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)
    print("\nИзменения сохранены!")


def add_note():
    title = input("\nВведите заголовок заметки: ")
    text = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": len(notes) + 1, "title": title, "text": text, "timestamp": timestamp}
    notes.append(note)
    print("Заметка успешно добавлена!")
    save_file(notes)


def delete_note():
    print_notes(notes)
    note_id = int(input("Введите номер заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            print("Заметка успешно удалена!")
            save_file(notes)
            return
    print("Заметка с указанным номером не найдена!\n")


def edit_note():
    print_notes(notes)
    note_id = int(input("Введите номер заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            new_title = input("\nВведите новый заголовок заметки: ")
            new_text = input("Введите новый текст заметки: ")
            if new_title:
                note["title"] = new_title
            if new_text:
                note["text"] = new_text
            note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Заметка успешно изменена!")
            save_file(notes)
            return
    print("Заметка с указанным номером не найдена!\n")


def filter_notes_by_date():
    date_str = input("Введите дату для фильтрации заметок (YYYY-MM-DD): ")
    try:
        filter_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Некорректный формат даты\n")
        return

    filtered_notes = [
        note
        for note in notes
        if datetime.datetime.strptime(note["timestamp"], "%Y-%m-%d %H:%M:%S").date()
        == filter_date
    ]

    if filtered_notes:
        print("Заметки на указанную дату:")
        print_notes(filtered_notes)
    else:
        print("Заметок на указанную дату нет!")


def print_notes(notes):
    if notes:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['text']}")
            print(f"Дата/Время: {note['timestamp']}")
            print()
    else:
        print("\nНет данных для вывода!")


def menu():
    menu_points = [
        "Посмотреть все заметки",
        "Добавить заметку",
        "Редактировать заметку",
        "Удалить заметку",
        "Найти заметку",
        "Сохранить файл",
        "Выход",
    ]
    [print(f"\t{i}. {item}") for i, item in enumerate(menu_points, 1)]
    choise = int(input("\nВыберите требуемый пункт меню: "))
    return choise


while True:
    print()
    choise = menu()
    match choise:
        case 1:
            print_notes(notes)
            print()
        case 2:
            add_note()
        case 3:
            edit_note()
        case 4:
            delete_note()
        case 5:
            filter_notes_by_date()
        case 6:
            save_file(notes)
        case 7:
            print("До новых встреч!\n")
            break

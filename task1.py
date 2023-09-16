import json
import os
from datetime import datetime

# Путь к файлу с заметками
NOTES_FILE = "notes.json"

# Проверяем, существует ли файл с заметками, и создаем его, если нет
if not os.path.exists(NOTES_FILE):
    with open(NOTES_FILE, "w") as file:
        json.dump([], file)

def load_notes():
    with open(NOTES_FILE, "r") as file:
        return json.load(file)

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_note(title, body):
    notes = load_notes()
    note_id = len(notes) + 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_note = {
        "id": note_id,
        "title": title,
        "body": body,
        "timestamp": timestamp,
    }
    notes.append(new_note)
    save_notes(notes)
    print("Заметка добавлена.")

def edit_note(note_id, title, body):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = title
            note["body"] = body
            note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")

def delete_note(note_id):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка удалена.")
            return
    print("Заметка с указанным ID не найдена.")

def list_notes():
    notes = load_notes()
    if not notes:
        print("Список заметок пуст.")
        return
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Тело: {note['body']}")
        print(f"Дата/время создания или изменения: {note['timestamp']}")
        print("-" * 40)

while True:
    print("\nВыберите действие:")
    print("1. Добавить заметку")
    print("2. Редактировать заметку")
    print("3. Удалить заметку")
    print("4. Список заметок")
    print("5. Выйти")
    
    choice = input("Введите номер действия: ")
    
    if choice == "1":
        title = input("Введите заголовок: ")
        body = input("Введите тело заметки: ")
        add_note(title, body)
    elif choice == "2":
        note_id = int(input("Введите ID заметки для редактирования: "))
        title = input("Введите новый заголовок: ")
        body = input("Введите новое тело заметки: ")
        edit_note(note_id, title, body)
    elif choice == "3":
        note_id = int(input("Введите ID заметки для удаления: "))
        delete_note(note_id)
    elif choice == "4":
        list_notes()
    elif choice == "5":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")

import json
import os
import datetime

notes = [] 

# Чтения заметок из файла
def read_notes():
    global notes
    if os.path.exists('notes.json'):
        with open('notes.json', 'r') as f:
            notes = json.load(f)

# Cохранения заметок в файл
def save_notes():
    with open('notes.json', 'w') as f:
        json.dump(notes, f, indent=4)

# Добавления заметки
def add_note():
    title = input('Введите заголовок заметки: ')
    body = input('Введите текст заметки: ')
    note = {
        'id': len(notes) + 1,
        'title': title,
        'body': body,
        'created_at': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    notes.append(note)
    save_notes()

# Редактирования заметки
def edit_note():
    note_id = int(input('Введите ID заметки для редактирования: '))
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        title = input('Введите заголовок заметки: ')
        body = input('Введите текст заметки: ')
        note['title'] = title
        note['body'] = body
        note['updated_at'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        save_notes()
    else:
        print('Заметка не найдена')

# Удаления заметки
def delete_note():
    note_id = int(input('Введите ID заметки для удаления: '))
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        notes.remove(note)
        save_notes()
    else:
        print('Заметка не найдена')

# Вывод списка заметок
def show_notes():
    for note in notes:
        print(f"{note['id']}. {note['title']} ({note['created_at']})")

# Фильтр
def filter_notes():
    while True:
            date_str = input('Введите дату (гггг-мм-дд): ')
            try:
                date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                break
            except ValueError:
                print('Неверный формат даты. Попробуйте снова.')
    filters_notes = [note for note in notes if datetime.datetime.strptime(note['created_at'], '%Y-%m-%d %H:%M:%S').date() == date.date()]
    if len(filters_notes) == 0:
            print('Заметки не найдены')
    else:
        for note in filters_notes:
            print(f"{note['id']}. {note['title']} ({note['created_at']})")
        
        

read_notes()

while True:
    print('Что вы хотите сделать?')
    print('1. Добавить заметку')
    print('2. Редактировать заметку')
    print('3. Удалить заметку')
    print('4. Вывести список заметок')
    print('5. Фильтр заметок по дате')
    print('6. Выход')
    n = input('Введите номер действия: ')
    if n == '1':
        add_note()
    elif n == '2':
        edit_note()
    elif n == '3':
        delete_note()
    elif n == '4':
        show_notes()
    elif n == '5':
        filter_notes()
    elif n == '6':
        break
    else:
        print('Не верный ввод. Введите цыфры от 0 до 6')


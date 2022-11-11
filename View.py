

def show_menu():
    print('1. Показать все контакты')
    print('2. Открыть файл с контактами')
    print('3. Добавить контакт')
    print('4. Изменить контакт')
    print('5. Удалить контакт')
    print('6. Поиск по контактам')

    choise = int(input('Выберите пункт меню: '))
    return choise

def show_phone_book():
    if len(phone_book) < 1:
        print('Телефонная книга пуста')
    else:
        for item in phone_book:
            print(item)

def input_path():
    path = input('Введите имя файла: ')
    return path



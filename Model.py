import Controler

phone_book = []

def get_phone_book():
    global phone_book
    return phone_book

def open_file(path):
    global phone_book 
    with open('phone.txt', 'r', encoding='UTF-8') as file:
        data = file.readlines()
        #print(data)
        for item in data:
            contact = item.replace('\n', '').split(';')
            phone_book.append(contact)

def add_contact(contact):
    global phone_book
    phone_book.append(list(contact))
    #print(contact)

def change_contact(id, choise, value):
    global phone_book
    phone_book [int(id)][int(choise)] = value

def delete_contact(id):
    global phone_book
    del phone_book[id]
    return phone_book
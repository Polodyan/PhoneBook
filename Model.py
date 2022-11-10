import Controler

phone_book = []

def get_phone_book():
    global phone_book
    return phone_book

def open_file(path):
    global phone_book 
    with open('C:\Users\Полина\Desktop\Phone_book\phone_b.txt', 'r', encoding='UTF-8') as file:
        data = file.readlines()
        print(data)
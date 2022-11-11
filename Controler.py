import View, Model

def start():
    choise = 1
    while choise != 9:
        choise = View.show_menu()
        match(choise):
            case 0:
                phone_book = Model.get_phone_book()
                View.show_phone_book(phone_book)
            case 1:
                path = View.input_path()
                Model.open_file(path) 
            case 2:
                pass
            case 3: 
                contact = View.input_contact()
                Model.add_contact(contact)    
            case 4:
                contact = View.input_change()
                Model.change_contact(*contact)
            
            case 5:
                id = view.input_delete()
                model.delete_contact(id)
                
            case 6:
               contact=view.search_contact(phone_book)
               
            case _:# exit
                return False
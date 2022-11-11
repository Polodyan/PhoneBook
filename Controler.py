import View, Model

def start():
   choise = View.show_menu()
   match(choise):
    case 1:
        phone_book = Model.get_phone_book()
        View.show_phone_book(phone_book)
    case 2:
        path = View.input_path()
        Model.open_file(path)
#   case 3:
#       addContact()
#    case 4:
#        changeContact()
#    case 5:
#        deleteContact()
#    case 6:
#        findContact()
#    case _:
#        break
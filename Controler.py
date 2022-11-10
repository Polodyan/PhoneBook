import View, Model

def start():
   choise = View.show_menu()
   match(choise):
    case 1:
        View.show_phone_book()
    case 2:
        path = View.input_path()
        Model.open_file(path)
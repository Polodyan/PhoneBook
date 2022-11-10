import View, Model

def start():
   choice = View.show_menu()
   match(choice):
    case 1:
        View.show_phone_book()
    case 2:
        path = View.input_path()
        Model.open_file(path)
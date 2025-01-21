from controller import Controller
from view import View
from model import DictionaryProcessor


if __name__ == "__main__":
    processor = DictionaryProcessor()
    view = View(processor)
    controller = Controller(view)
    controller.user_menu()
from controller import Controller
from view import View
from model import DictionaryProcessor


if __name__ == "__main__":
    processor = DictionaryProcessor()
    controller = Controller(processor, None)
    view = View(controller)
    controller.view = view
    view.user_menu()
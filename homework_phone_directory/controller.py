class Controller:

    def __init__(self, view):
        self.view = view

    def user_menu(self):
        while True:
            menu_item = input('Введите интересующий вас пункт меню:\n'
                              '1. Показать все контакты\n'
                              '2. Создать контакт\n'
                              '3. Найти контакт\n'
                              '4. Изменить контакт\n'
                              '5. Удалить контакт\n'
                              '6. Сохранить файл\n'
                              '7. Выход\n')
            self.view.process_command(menu_item)
    @staticmethod
    def get_contact_data():
        name = input('Enter name: ')
        second_name = input('Entet second name: ')
        phone_number = input('Enter phone number: ')
        city = input('Enter city: ')
        return name, second_name, phone_number, city


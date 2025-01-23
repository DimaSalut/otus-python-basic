from tkinter.font import names


class View:

    def __init__(self, controller):
        self.controller = controller

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
            self.controller.process_command(menu_item)

    @staticmethod
    def get_contact_data():
        name = input('Enter name: ')
        second_name = input('Enter second name: ')
        phone_number = input('Enter phone number: ')
        city = input('Enter city: ')
        return {
            'name': name,
            'second_name': second_name,
            'phone_number': phone_number,
            'city': city
        }

    @staticmethod
    def contact_data_for_find():
        name = input('Enter name: ')
        second_name = input('Enter second name: ')
        return {
            'name': name,
            'second_name': second_name
        }





    # def process_command(self, command_number):
    #     if command_number == '1':
    #         self.dict.show_contacts()
    #     elif command_number == '2':
    #         self.dict.create_contact()
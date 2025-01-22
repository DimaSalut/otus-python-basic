class Controller:

    def __init__(self, processor, view):
        self.processor = processor
        self.view = view


    def process_command(self, command_number):
        if command_number == '1':
            self.processor.show_contacts()
        elif command_number == '2':
            self.processor.create_contact(self.view.get_contact_data())
            print('Contact successfully created')
        elif command_number == '3':
            pass
        elif command_number == '7':
            print('Exit the program')
            exit()




    # def user_menu(self):
    #     while True:
    #         menu_item = input('Введите интересующий вас пункт меню:\n'
    #                           '1. Показать все контакты\n'
    #                           '2. Создать контакт\n'
    #                           '3. Найти контакт\n'
    #                           '4. Изменить контакт\n'
    #                           '5. Удалить контакт\n'
    #                           '6. Сохранить файл\n'
    #                           '7. Выход\n')
    #         self.view.process_command(menu_item)


    # def get_contact_data(self):
    #     name = input('Enter name: ')
    #     second_name = input('Enter second name: ')
    #     phone_number = input('Enter phone number: ')
    #     city = input('Enter city: ')
    #     self.view.dict.create_contact(name, second_name, phone_number, city)


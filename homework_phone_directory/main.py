import json, os, menu
path = os.path.join(os.path.dirname(__file__), 'contacts_100.json')
id_number = 1


def open_file():
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data
    else:
        print(f'{path} does not exists')


def show_contacts(data):
    for i in data:
        for key, value in i.items():
            print(f'{key}: {value}')
        print('\n')
    return data


def find_contact():
    find_name = input('Enter name for found: ')
    find_surname = input('Enter second name for found: ')
    data = open_file()
    found_user = [i for i in data if i['Имя'] == find_name and i['Фамилия'] == find_surname]
    if found_user:
        show_contacts(found_user)
    else:
        print('User was not found')
    return found_user


def find_contact_by_id(contact_id):
    data = open_file()
    for i in data:
        if i['id'] == contact_id:
            return i
    return 'ID was not found'


def save_file(saved_file):
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(saved_file, json_file, ensure_ascii=False, indent=4)
    return saved_file


def assign_user_id():
    global id_number
    data = open_file()
    for i in data:
        i['id'] = id_number
        id_number += 1
    save_file(data)


def process_file():
    global id_number
    while True:
        user_choice = menu.user_menu()
        if user_choice == '1':
            data = open_file()
            show_contacts(data)
        elif user_choice == '2':
            name = input('Enter name: ')
            second_name = input('Enter second name: ')
            phone_number = input('Enter phone number: ')
            city = input('Enter city: ')
            data = open_file()
            data.append({"Имя": name,
                         'Фамилия': second_name,
                         'Номер телефона': phone_number,
                         'Город': city,
                         'id': len(data) + 1})
            save_file(data)
        elif user_choice == '3':
            find_contact()
        elif user_choice == '4':
            data = open_file()
            show_contacts(data)
            contact_id = int(input("Enter the ID of the contact you want to change: "))
            contact_to_change = find_contact_by_id(contact_id)
            change_choice = input('1.Change name\n'
                                  '2.Change surname\n'
                                  '3.Change phone number\n'
                                  '4.Change city\n')
            if change_choice == '1':
                change_name = input('Enter the contact name to change: \n')
                contact_to_change['Имя'] = change_name
            elif change_choice == '2':
                change_name = input('Enter the contact surname to change: \n')
                contact_to_change['Фамилия'] = change_name
            elif change_choice == '3':
                change_phone_number = input('Enter the contact phonenumber to change: \n')
                contact_to_change['Номер телефона'] = change_phone_number
            elif change_choice == '4':
                change_city = input('Enter the contact city to change: \n')
                contact_to_change['Город'] = change_city
            else:
                print('You entered non valid value')
            for index, dictionary in enumerate(data):
                if dictionary['id'] == contact_id:
                    data[index] = contact_to_change
                    print('Contact was changed')
            save_file(data)
        elif user_choice == '5':
            data = open_file()
            show_contacts(data)
            contact_id_to_delete = int(input('Enter the contact id to delete: \n'))
            found = False
            for index, dictionary in enumerate(data):
                if dictionary['id'] == contact_id_to_delete:
                    del data[index]
                    print('Contacts was deleted')
                    found = True
                    break
            if not found:
                print('ID was not found')
            save_file(data)
            assign_user_id()
        elif user_choice == '6':
            data = open_file()
            save_file(data)
        elif user_choice == '7':
            break
        else:
            print('Вы ввели некорректное значение')


process_file()
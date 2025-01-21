import json, os, controller

path = os.path.join(os.path.dirname(__file__), 'contacts_100.json')

class Contact:
    base_id_number = 0
    def __init__(self, name=None, second_name=None, phone_number=None, city=None):
        self.name = name
        self.second_name = second_name
        self.phone_number = phone_number
        self.city = city
        self.id_number = Contact.initial_id()


    def to_dict(self):
        return {
            'Имя': self.name,
            'Фамилия': self.second_name,
            'Номер телефона': self.phone_number,
            'Город': self.city,
            'id': self.id_number
        }


    @classmethod
    def initial_id(cls):
        cls.base_id_number += 1
        return cls.base_id_number


    def __str__(self):
        return (f'Name: {self.name}\nSecond name: {self.second_name}\nPhone number: {self.phone_number}\n'
                f'City: {self.city}\nId: {self.id_number}')


class File:

    @staticmethod
    def open_file():
        if os.path.exists:
            with open(path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                return data

    @staticmethod
    def save_file(saved_file):
        with open(path, 'w', encoding='utf-8') as json_file:
            json.dump(saved_file, json_file, ensure_ascii=True, indent = 4)


class DictionaryProcessor:

    def __init__(self):
        self.file = File()
        self.contacts = self.file.open_file()


    def show_contacts(self):

        for item in self.file.open_file():
            contact_obj = Contact(name=item['Имя'], second_name=item['Фамилия'], phone_number=item['Номер телефона'],
                                  city=item['Город'])
            print(contact_obj, '\n')

    def create_contact(self, name, second_name, phone_number, city):
        new_contact = Contact(name=name, second_name=second_name, phone_number=phone_number, city=city)
        self.contacts.append(new_contact.to_dict())

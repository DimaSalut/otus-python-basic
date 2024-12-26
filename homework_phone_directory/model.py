import json, os
from dataclasses import dataclass


path = os.path.join(os.path.dirname(__file__), 'contacts_100.json')

class Contact:
    base_id_number = 0
    def __init__(self, name=None, second_name=None, phone_number=None, city=None):
        self.name = name
        self.second_name = second_name
        self.phone_number = phone_number
        self.city = city
        self.id_number = Contact.initial_id()

    @classmethod
    def initial_id(cls):
        cls.base_id_number += 1
        return cls.base_id_number


    def __str__(self):
        return (f'Name: {self.name}\nSecond name: {self.second_name}\nPhone number: {self.phone_number}\n'
                f'City: {self.city}\nId: {self.id_number}')


class File:
    # path = os.path.join(os.path.dirname(__file__), 'contacts_100.json')
    @classmethod
    def open_file(cls):
        if os.path.exists:
            with open(path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                return data

    @classmethod
    def save_file(cls, saved_file):
        with open(path, 'w', encoding='utf-8') as json_file:
            json.dump(saved_file, json_file, ensure_ascii=True, indent = 4)


class Dictionary:
    pass

a = Contact(name='Jhon')
b = Contact(name='Artem')
print(a)
print(b)

from controller import user_menu
from homework_phone_directory.model import Dictionary

if user_menu() == '1':
    Dictionary.show_contacts()


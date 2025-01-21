class View:

    def __init__(self, dict):
        self.dict = dict

    def process_command(self, command_number):
        if command_number == '1':
            self.dict.show_contacts()
        elif command_number == '2':
            self.dict.create_contact()
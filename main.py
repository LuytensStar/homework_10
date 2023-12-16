from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    def __init__(self, name):
        self.value = name

    def __str__(self):
        return self.value

class Phone(Field):
    def __init__(self, phone):
        if not (len(phone) == 10 and phone.isdigit()):
            raise ValueError("Phone number must be 10 digits")
        self.value = phone

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break

    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError("Phone number not found")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None   
    def __str__(self):
        phones = "; ".join([str(phone.value) for phone in self.phones])
        return f"Contact name: {self.name.value}, phones: {phones}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
from collections import UserDict
import re
class Field:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)
class Phone(Field):
    def __init__(self, value):
        self.validate_phone(value)
        super().__init__(value)
    def validate_phone(self, value):
        if not re.match(r'^\d{10}$', value):
            raise ValueError("Phone number must be 10 digits long")
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_to_remove = next((p for p in self.phones if p.value == phone), None)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
    def edit_phone(self, old_phone, new_phone):
        phone_to_edit = next((p for p in self.phones if p.value == old_phone), None)
        if phone_to_edit:
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
    def find_phone(self, phone):
        return next((p.value for p in self.phones if p.value == phone), None)
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    def find(self, name):
        return self.data.get(name)
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        def __str__(self):
            return '\n'.join(str(record) for record in self.data.values())
        
###

# Створення нової адресної книги
if __name__ == "__main__":
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    print("Address Book:")
    print(book)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")

    print("\nUpdated John Record:")
    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"\nFound Phone for John: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

    print("\nAddress Book after deleting Jane:")
    print(book)
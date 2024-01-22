from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # Клас для представлення поля "Ім'я" в записі контакту
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    # Клас для представлення поля "Телефон" в записі контакту
    def __init__(self, phone):
        # Валідація телефонного номера
        validation = True
        for elem in phone:
            if elem.isdigit():
                continue
            else:
                validation = False
                break
        if len(phone) != 10:
            validation = False
        if validation:
            super().__init__(phone)
        else:
            raise ValueError('Phone is not valid')


class Record:
    def __init__(self, name):
        # Ініціалізація запису контакту з ім'ям та порожним списком телефонів
        self.name = Name(name)
        self.phones = []

    # Додавання нового телефонного номера до запису контакту
    def add_phone(self, phone):
        valid_phone = Phone(phone)
        if valid_phone.value is not None:
            self.phones.append(valid_phone)
        else:
            return 'Phone is not valid'

    # Видалення телефонного номера з запису контакту
    def remove_phone(self, phone):
        valid_phone = Phone(phone)
        phone_to_remove = None
        for ph in self.phones:
            if ph.value == valid_phone.value:
                phone_to_remove = ph
                break

        if phone_to_remove is not None:
            self.phones.remove(phone_to_remove)
        else:
            return 'This contact doesn\'t have this phone'

    # Редагування телефонного номера в записі контакту
    def edit_phone(self, old_phone_value, new_phone_value):
        old_phone_index = None
        for i, ph in enumerate(self.phones):
            if ph.value == old_phone_value:
                old_phone_index = i
                break

        if old_phone_index is not None:
            new_phone = Phone(new_phone_value)
            if new_phone.value is not None:
                self.phones[old_phone_index] = new_phone
            else:
                return 'New phone is not valid'
        else:
            raise ValueError('Phone not found')

    # Пошук телефонного номера в записі контакту
    def find_phone(self, phone):
        valid_phone = Phone(phone)
        for ph in self.phones:
            if ph.value == valid_phone.value:
                return ph
        return None

    # Перетворення об'єкту Record у рядок для виведення
    def __str__(self):
        phones_str = '; '.join(str(p) for p in self.phones)
        return f"Contact name: {self.name}, phones: {phones_str}"


class AddressBook(UserDict):
    # Клас для представлення телефонної книги, яка є словником записів контактів
    def add_record(self, record):
        # Додавання нового запису контакту до телефонної книги
        if isinstance(record, Record):
            self.data[record.name.value] = record
        else:
            raise ValueError("Here you can add only records")

    # Пошук запису контакту в телефонній книзі за ім'ям
    def find(self, name):
        return self.data.get(name, None)

    # Видалення запису контакту з телефонної книги за ім'ям
    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
        else:
            print(f"This contact doesn't exist")


from decorators import input_error, attrs_count

@input_error
@attrs_count(2, 'Give me name and phone please.')
def add_contact(args: list, contacts: dict) -> str:
    """Додає контакт до словника"""
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
@attrs_count(2, 'Give me name and phone please.')
def change_contact(args: list, contacts: dict) -> str:
    """Змінює номер телефону існуючого контакту"""
    name, phone = args # тут мала бути помилка яка оброблена input_error
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."


@input_error
@attrs_count(1, 'Give me name please.')
def get_contact(args: list, contacts: dict) -> str:
    """Повертає номер телефону за ім'ям контакту"""
    name = args[0] # тут мала бути помилка яка оброблена input_error
    if name not in contacts:
        raise KeyError
    return contacts[name]


@input_error
def get_all_contacts(contacts: dict) -> str:
    """Виводить усі збережені контакти"""
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

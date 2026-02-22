from contact_manager import (
    add_contact,
    change_contact,
    get_contact,
    get_all_contacts,
)

def parse_input(user_input: str) -> tuple:
    """Розбирає введення користувача на команду та аргументи"""
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args


def main():
    """Головний цикл бота-помічника"""
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_contact(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()

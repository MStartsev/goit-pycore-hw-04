from src.constants import *
from src.handlers import *
from src.utils import parse_input


def main():
    """Головна функція бота"""
    contacts = {}
    print(WELCOME_MESSAGE)

    while True:
        user_input = input("Enter a command: ")
        try:
            command, *args = parse_input(user_input)

            if command in EXIT_COMMANDS:
                print(GOODBYE_MESSAGE)
                break
            elif command == HELLO_COMMAND:
                print(HELP_MESSAGE)
            elif command == ADD_COMMAND:
                print(add_contact(args, contacts))
            elif command == CHANGE_COMMAND:
                print(change_contact(args, contacts))
            elif command == PHONE_COMMAND:
                print(show_phone(args, contacts))
            elif command == ALL_COMMAND:
                print(show_all(contacts))
            else:
                print(INVALID_COMMAND_MESSAGE)

        except (ValueError, IndexError):
            print(INVALID_FORMAT_MESSAGE)


if __name__ == "__main__":
    main()

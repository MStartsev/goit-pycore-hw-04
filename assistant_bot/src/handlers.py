from src.constants import *


def add_contact(args: list, contacts: dict) -> str:
    """Додає новий контакт"""
    name, phone = args
    if name in contacts:
        return CONTACT_EXISTS
    contacts[name] = phone
    return CONTACT_ADDED


def change_contact(args: list, contacts: dict) -> str:
    """Змінює існуючий контакт"""
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return CONTACT_UPDATED
    return CONTACT_NOT_FOUND


def show_phone(args: list, contacts: dict) -> str:
    """Показує телефон для контакту"""
    name = args[0]
    return contacts.get(name, CONTACT_NOT_FOUND)


def show_all(contacts: dict) -> str:
    """Показує всі контакти"""
    if not contacts:
        return NO_CONTACTS
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

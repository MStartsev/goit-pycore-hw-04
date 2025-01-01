def parse_input(user_input: str) -> tuple:
    """
    Парсить введену користувачем команду.

    Args:
        user_input (str): Рядок введення користувача

    Returns:
        tuple: Команда та її аргументи
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

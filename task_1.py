def total_salary(path):
    """
    Обчислює загальну та середню заробітну плату розробників з файлу.

    Args:
        path (str): Шлях до файлу із зарплатами

    Returns:
        tuple: (Загальна сума, Середня зарплата)
    """
    try:
        total = 0
        count = 0

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    _, salary = line.strip().split(",")
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Помилка формату в рядку: {line}")
                    continue

        if count == 0:
            return 0, 0

        average = total / count
        return total, average

    except FileNotFoundError:
        print(f"Файл {path} не знайдено")
        return 0, 0

def get_cats_info(path):
    """
    Читає файл з інформацією про котів та повертає список словників.

    Args:
        path (str): Шлях до файлу

    Returns:
        list: Список словників з інформацією про котів
    """
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(",")
                    cats.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    print(f"Помилка в рядку: {line}")
                    continue

        return cats

    except FileNotFoundError:
        print(f"Файл {path} не знайдено")
        return []

import sys
from pathlib import Path
from colorama import init, Fore, Style

init()


def display_directory_structure(directory_path, prefix=""):
    """
    Рекурсивно відображає структуру директорії.

    Args:
        directory_path: Шлях до директорії
        prefix: Префікс для відступів
    """

    try:
        path = Path(directory_path)

        if not path.exists():
            print(f"Помилка: шлях {directory_path} не існує")
            return

        if not path.is_dir():
            print(f"Помилка: {directory_path} не є директорією")
            return

        items = sorted(path.iterdir())

        for item in items:
            if item.is_dir():
                print(f"{prefix}📂 {Fore.BLUE}{item.name}{Style.RESET_ALL}")
                display_directory_structure(item, prefix + "  ")
            else:
                print(f"{prefix}📄 {Fore.GREEN}{item.name}{Style.RESET_ALL}")

    except PermissionError:
        print(f"Помилка: немає доступу до {directory_path}")
    except Exception as e:
        print(f"Помилка: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Використання: python script.py <шлях_до_директорії>")
        sys.exit(1)

    directory_path = sys.argv[1]
    print(f"\nСтруктура директорії: {directory_path}\n")
    display_directory_structure(directory_path)

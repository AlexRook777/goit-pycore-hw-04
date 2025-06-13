import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація Colorama для коректної роботи кольорів у різних терміналах (особливо на Windows)
init(autoreset=True)

def print_directory_structure(path: Path, indent: int = 0):
    indent_str = "│   " * indent # Символ для відступу

    # Перевіряємо, чи це директорія
    if path.is_dir():
        print(f"{indent_str}{Fore.BLUE}📂 {path.name}{Style.RESET_ALL}")
        # Якщо це директорія, рекурсивно обходимо її вміст
        for item in sorted(path.iterdir()): # Сортуємо для консистентного виводу
            print_directory_structure(item, indent + 1)
    # Якщо це файл
    elif path.is_file():
        print(f"{indent_str}{Fore.GREEN}📜 {path.name}{Style.RESET_ALL}")
    # Обробка інших типів об'єктів (наприклад, символічних посилань), якщо вони зустрічаються
    else:
        print(f"{indent_str}{Fore.WHITE}{path.name}{Style.RESET_ALL} (інший тип)")

def main():
    # Перевірка наявності аргументу командного рядка
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: Будь ласка, вкажіть шлях до директорії як аргумент.")
        print(f"Приклад використання: python {sys.argv[0]} /шлях/до/вашої/директорії{Style.RESET_ALL}")
        sys.exit(1) # Вихід з кодом помилки

    # Отримання шляху з аргументу командного рядка
    target_path_str = sys.argv[1]
    target_path = Path(target_path_str)

    # Перевірка, чи шлях існує
    if not target_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{target_path_str}' не існує.{Style.RESET_ALL}")
        sys.exit(1)

    # Перевірка, чи шлях веде до директорії
    if not target_path.is_dir():
        print(f"{Fore.RED}Помилка: Шлях '{target_path_str}' не є директорією.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.CYAN}Структура директорії: {target_path_str}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}--- Початок візуалізації ---{Style.RESET_ALL}")
    print_directory_structure(target_path)
    print(f"{Fore.CYAN}--- Кінець візуалізації ---{Style.RESET_ALL}")

if __name__ == "__main__":
    main()


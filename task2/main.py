from pathlib import Path

# Функція для отримання інформації про котів з файлу
def get_cats_info(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file: # відкриваємо файл для читання
            cats = [line.strip().split(',') for line in file if line.strip()]    # читаємо дані з файлу, розділяючи рядки за комами
        cats_info = [{'id': str(cat[0]), 'name': str(cat[1]), 'age': int(cat[2])} for cat in cats] # перетворюємо дані у список словників
        return cats_info
    except FileNotFoundError: # обробка помилки, якщо файл не знайдено
        print(f"Файл {file_path} не знайдено.")
        return {}
    except ValueError: # обробка помилки, якщо дані у файлі не можуть бути перетворені на int
        print("Помилка у форматі даних у файлі.")
        return {}
    except IndexError: # обробка помилки, якщо рядок не містить достатньо елементів
        print("Помилка у форматі рядків у файлі.")
        return {}
    
    

# Example usage
# Вказуємо шлях до файлу salary.csv
file_name = Path.cwd() / "task2" / "cats.csv"
# Виклик функції для обчислення загальної та середньої заробітної плати
cats = get_cats_info(file_name)
print(cats) 




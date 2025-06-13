from pathlib import Path

# Функція для обчислення загальної та середньої заробітної плати з файлу
def total_salary(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file: # відкриваємо файл для читання
         # читаємо дані з файлу, розділяючи рядки за комами
            salaries = [float(line.strip().split(',')[1]) for line in file if line.strip()] 
        total = round(sum(salaries),2) # обчислюємо загальну заробітну плату, округляючи до двох знаків після коми
        average = round(total / len(salaries) if salaries else 0 , 2) # обчислюємо середню заробітну плату, округляючи до двох знаків після коми 
        return total, average
    except FileNotFoundError: # обробка помилки, якщо файл не знайдено
        print(f"Файл {file_path} не знайдено.")
        return 0, 0 
    except ValueError: # обробка помилки, якщо дані у файлі не можуть бути перетворені на float 
        print("Помилка у форматі даних у файлі.")
        return 0, 0 
    except IndexError: # обробка помилки, якщо рядок не містить достатньо елементів
        print("Помилка у форматі рядків у файлі.")
        return 0, 0
    

# Example usage
# Вказуємо шлях до файлу salary.csv
file_name = Path.cwd() / "task1" / "salary.csv"
# Виклик функції для обчислення загальної та середньої заробітної плати
total, average = total_salary(file_name)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


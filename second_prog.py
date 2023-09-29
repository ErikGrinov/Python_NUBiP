import pandas as pd
import csv
from datetime import date


# Функція для обчислення віку на основі дати народження та поточної дати
def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


try:
    # Зчитуємо дані з CSV-файлу
    df = pd.read_csv('employees.csv', encoding='utf-8')

    # Додаємо стовпець "Вік" до DataFrame
    df['Дата народження'] = pd.to_datetime(df['Дата народження'])
    df['Вік'] = df['Дата народження'].apply(calculate_age)

    # Створюємо Excel-файл з декількома аркушами
    with pd.ExcelWriter('employees.xlsx', engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='all', index=False)

        # Розділяємо дані на вікові категорії і записуємо на відповідні аркуши
        df_under_18 = df[df['Вік'] < 18]
        df_18_to_45 = df[(df['Вік'] >= 18) & (df['Вік'] <= 45)]
        df_45_to_70 = df[(df['Вік'] > 45) & (df['Вік'] <= 70)]
        df_over_70 = df[df['Вік'] > 70]

        df_under_18.to_excel(writer, sheet_name='younger_18', index=False)
        df_18_to_45.to_excel(writer, sheet_name='18-45', index=False)
        df_45_to_70.to_excel(writer, sheet_name='45-70', index=False)
        df_over_70.to_excel(writer, sheet_name='older_70', index=False)

    print("Ok, програма завершила свою роботу успішно.")

except FileNotFoundError:
    print("Помилка: файл CSV не знайдено або не вдалося відкрити.")
except Exception as e:
    print(f"Помилка: {str(e)}")
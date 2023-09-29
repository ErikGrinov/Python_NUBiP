import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Функція для обчислення віку на основі дати народження
def calculate_age(birthdate):
    try:
        birthdate = pd.to_datetime(birthdate, errors='coerce')
        if pd.notnull(birthdate):
            today = datetime.now()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            return age
    except Exception as e:
        pass
    return None

try:
    # Зчитуємо дані з CSV-файлу
    df = pd.read_csv('employees.csv', encoding='utf-8')

    # Виводимо повідомлення про завантаження
    print("Файл CSV успішно завантажено.")

    # Рахуємо кількість співробітників чоловічої і жіночої статі
    gender_counts = df['Стать'].value_counts()

    # Розділяємо дані на вікові категорії
    age_bins = [0, 18, 45, 70, float('inf')]
    age_labels = ['<18', '18-45', '45-70', '70+']
    df['Вік'] = df['Дата народження'].apply(calculate_age)
    df['Вікова категорія'] = pd.cut(df['Вік'], bins=age_bins, labels=age_labels)
    age_category_counts = df['Вікова категорія'].value_counts()

    # Рахуємо кількість співробітників жіночої та чоловічої статі в кожній віковій категорії
    gender_age_counts = df.groupby(['Стать', 'Вікова категорія']).size().unstack(fill_value=0)

    # Діаграма 1: Розподіл співробітників за статтю
    plt.figure(figsize=(12, 4))
    plt.subplot(131)
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
    plt.title('Розподіл співробітників за статтю')

    # Діаграма 2: Розподіл співробітників за віком
    plt.subplot(132)
    sns.countplot(data=df, x='Вікова категорія', order=age_labels)
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість співробітників')
    plt.title('Розподіл співробітників за віком')

    # Діаграма 3: Розподіл співробітників за статтю і віком
    plt.subplot(133)
    gender_age_counts.plot(kind='bar', stacked=True, figsize=(12, 4))
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість співробітників')
    plt.title('Розподіл співробітників за віком та статтю')
    plt.legend(title='Стать', loc='upper right')

    plt.tight_layout()
    plt.show()

    print("Ok, програма завершила свою роботу успішно.")

except FileNotFoundError:
    print("Помилка: файл CSV не знайдено або не вдалося відкрити.")
except Exception as e:
    print(f"Помилка: {str(e)}")
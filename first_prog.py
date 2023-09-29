import csv
import random
from faker import Faker
from datetime import date

# Ініціалізуємо генератор фейкових даних
fake = Faker('uk_UA')

# Функція для генерації випадкової дати народження
def generate_birthdate():
    return fake.date_of_birth(maximum_age=75, minimum_age=15).strftime('%Y-%m-%d')

# Відкриваємо CSV-файл для запису
with open('employees.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження', 'Посада',
                  'Місто проживання', 'Адреса проживання', 'Телефон', 'Email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Записуємо заголовки у файл
    writer.writeheader()

    # Генеруємо 40% жінок і 60% чоловіків
    total_records = 2000
    female_records = int(total_records * 0.4)
    male_records = total_records - female_records

    for _ in range(female_records):
        writer.writerow({
            'Прізвище': fake.last_name_female(),
            'Ім’я': fake.first_name_female(),
            'Стать': 'Жінка',
            'Дата народження': generate_birthdate(),
            'Посада': fake.job(),
            'Місто проживання': fake.city(),
            'Адреса проживання': fake.address(),
            'Телефон': fake.phone_number(),
            'Email': fake.email()
        })

    for _ in range(male_records):
        writer.writerow({
            'Прізвище': fake.last_name_male(),
            'Ім’я': fake.first_name_male(),
            'Стать': 'Чоловік',
            'Дата народження': generate_birthdate(),
            'Посада': fake.job(),
            'Місто проживання': fake.city(),
            'Адреса проживання': fake.address(),
            'Телефон': fake.phone_number(),
            'Email': fake.email()
        })

print("CSV-файл згенеровано успішно.")
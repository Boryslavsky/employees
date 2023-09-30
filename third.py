import csv
from datetime import datetime
from collections import Counter
import matplotlib.pyplot as plt

def calculate_age(birthdate):
    today = datetime.today()
    birthdate = datetime.strptime(birthdate, '%d-%m-%Y')
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def count_gender(data):
    gender_counts = Counter([row['Стать'] for row in data])
    return gender_counts['Чоловік'], gender_counts['Жінка'], gender_counts

def count_age_categories(data):
    age_categories = {'Молодше 18': 0, '18-45': 0, '45-70': 0, 'Старше 70': 0}
    today = datetime.today()

    for row in data:
        age = calculate_age(row['Дата народження'])
        if age < 18:
            age_categories['Молодше 18'] += 1
        elif 18 <= age <= 45:
            age_categories['18-45'] += 1
        elif 45 < age <= 70:
            age_categories['45-70'] += 1
        else:
            age_categories['Старше 70'] += 1

    return age_categories

def count_gender_in_age_categories(data):
    gender_age_counts = {
        'Молодше 18': {'Чоловік': 0, 'Жінка': 0},
        '18-45': {'Чоловік': 0, 'Жінка': 0},
        '45-70': {'Чоловік': 0, 'Жінка': 0},
        'Старше 70': {'Чоловік': 0, 'Жінка': 0}
    }

    today = datetime.today()

    for row in data:
        age = calculate_age(row['Дата народження'])
        gender = row['Стать']

        if age < 18:
            age_category = 'Молодше 18'
        elif 18 <= age <= 45:
            age_category = '18-45'
        elif 45 < age <= 70:
            age_category = '45-70'
        else:
            age_category = 'Старше 70'

        gender_age_counts[age_category][gender] += 1

    return gender_age_counts

def plot_bar_chart(data, title, x_label, y_label):
    labels = data.keys()
    values = data.values()

    plt.bar(labels, values)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

with open('formatted_employees.csv', newline='', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    data = list(reader)

male_count, female_count, gender_counts = count_gender(data)
print(f'Загальна кількість: {len(data)}, Чоловіків: {male_count}, Жінок: {female_count}')

age_categories = count_age_categories(data)
print('Кількість співробітників у вікових категоріях:')
for category, count in age_categories.items():
    print(f'{category}: {count}')

gender_age_counts = count_gender_in_age_categories(data)
print('Кількість співробітників чоловічої та жіночої статі у вікових категоріях:')
for category, counts in gender_age_counts.items():
    print(category)
    print(f'Чоловіків: {counts["Чоловік"]}, Жінок: {counts["Жінка"]}')

plot_bar_chart(gender_counts, 'Загальна кількість', 'Стать', 'Кількість')
plot_bar_chart(gender_age_counts['Молодше 18'], 'Співробітники молодше 18 років', 'Стать', 'Кількість')
plot_bar_chart(gender_age_counts['18-45'], 'Співробітники 18-45 років', 'Стать', 'Кількість')
plot_bar_chart(gender_age_counts['45-70'], 'Співробітники 45-70 років', 'Стать', 'Кількість')
plot_bar_chart(gender_age_counts['Старше 70'], 'Співробітники старше 70 років', 'Стать', 'Кількість')

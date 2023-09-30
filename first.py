import csv
import random
from faker import Faker

fake = Faker('uk_UA')

total_records = 2000
female_percentage = 40
male_percentage = 60

data = []
def remove_last(text):
    vowels = 'аеєиіоуюя'
    if text.endswith('й') or text[-1] in vowels:
        return text[:-1]
    return text

for _ in range(total_records):
    is_female = random.choices([True, False], weights=[female_percentage, male_percentage])[0]
    first_name = fake.first_name_female() if is_female else fake.first_name_male()
    last_name = fake.last_name_female() if is_female else fake.last_name_male()
    if is_female:
        ending = "івна"
    else:
        ending = "ович"
    middle_name = fake.first_name_male()
    if middle_name.endswith(('я', 'є', 'ю', 'ї','й')):
        middle_name = remove_last(middle_name)
        middle_name += "ївна" if is_female else "йович"
    else:
        middle_name = remove_last(middle_name)
        middle_name += ending
    gender = "Жінка" if is_female else "Чоловік"
    birthdate = fake.date_of_birth(minimum_age=15, maximum_age=85).strftime('%d-%m-%Y')
    position = fake.job()
    city = fake.city()
    address = fake.address()
    phone_number = fake.phone_number()
    email = fake.email()

    data.append([last_name, first_name, middle_name, gender, birthdate, position, city, address, phone_number, email])

with open('formatted_employees.csv', mode='w', newline='', encoding='utf-8-sig') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow(["Прізвище", "Ім’я", "По батькові", "Стать", "Дата народження", "Посада", "Місто проживання", "Адреса проживання", "Телефон", "Email"])
    writer.writerows(data)

print("CSV файл успішно створено у файлі 'formatted_employees.csv'.")

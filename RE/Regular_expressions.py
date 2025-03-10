import csv
import re
from pprint import pprint

# Чтение адресной книги
with open('phonebook_raw.csv', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# Функция для приведения ФИО в порядок
def fix_names(contacts_list):
    fixed_contacts = []
    for contact in contacts_list:
        full_name = list(filter(None, ' '.join(contact[:3]).split()))  # Убираем лишние пробелы
        while len(full_name) < 3:
            full_name.append('')  # Заполняем пустые значения, если их не хватает
        fixed_name = full_name + contact[3:]
        fixed_contacts.append(fixed_name)
    return fixed_contacts


# Функция для приведения телефонов к единому формату
def fix_phones(contacts_list):
    phone_pattern = re.compile(
        r'(\+7|8)\s*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*(\(?(доб\.?)\s*(\d+)\)?)?'
    )
    for contact in contacts_list:
        phone = contact[5]
        if phone:
            match = phone_pattern.search(phone)
            if match:
                formatted_phone = f"+7({match.group(2)}){match.group(3)}-{match.group(4)}-{match.group(5)}"
                if match.group(7) and match.group(8):
                    formatted_phone += f" доб.{match.group(8)}"
                contact[5] = formatted_phone
    return contacts_list


# Функция для объединения дублирующихся записей
def merge_duplicates(contacts_list):
    merged_contacts = {}
    for contact in contacts_list:
        key = (contact[0], contact[1])  # Фамилия + Имя как ключ
        if key in merged_contacts:
            for i in range(len(contact)):
                if contact[i]:  # Если в новой записи есть данные
                    if not merged_contacts[key][i] or len(contact[i]) > len(merged_contacts[key][i]):
                        merged_contacts[key][i] = contact[i]  # Берем более полное значение
        else:
            merged_contacts[key] = contact
    return list(merged_contacts.values())


# Применяем функции
contacts_list = fix_names(contacts_list)
contacts_list = fix_phones(contacts_list)
contacts_list = merge_duplicates(contacts_list)

# Сохранение результата в новый файл
with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)

print(len(contacts_list) - 1)
pprint(contacts_list)

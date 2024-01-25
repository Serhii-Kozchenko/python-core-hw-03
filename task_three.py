# Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату,
# залишаючи тільки цифри та символ '+' на початку.
# Функція приймає один аргумент - рядок з телефонним номером у будь-якому форматі та перетворює його на стандартний формат,
# залишаючи тільки цифри та символ '+'.
# Якщо номер не містить міжнародного коду, функція автоматично додає код '+38' (для України).
# Це гарантує, що всі номери будуть придатними для відправлення SMS.


import re


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "067\\t123 4567bbfgbdvSFVDFvsvdcdsds%'аегтив''''`V",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22и 11   ",
]


def normalize_phone(phone_number):
    pattern = r"[\d\+]+"
    phone_number = "".join(re.findall(pattern, phone_number))
    match len(phone_number):
        case 12:
            phone_number = "+" + phone_number
        case 10:
            phone_number = "+38" + phone_number
    return phone_number


sanitized_numbers = [normalize_phone(phone_number) for phone_number in raw_numbers]
print(sanitized_numbers)

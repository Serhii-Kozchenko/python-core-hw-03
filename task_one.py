# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

from datetime import datetime


def get_days_from_today(date: str):

    try:
        date_today = datetime.today()
        calculation_date = datetime.strptime(date, '%Y-%m-%d')
        result = calculation_date.toordinal() - date_today.toordinal()
        return result
       
    except Exception as error:
        print(f"Error: {error}")


print(get_days_from_today('2024-09-01'))
print(get_days_from_today('2024-01-01'))
print(get_days_from_today(2024))
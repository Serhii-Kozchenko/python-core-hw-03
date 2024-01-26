from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Bruce Willice", "birthday": "1990.01.30"},
]


def get_upcoming_birthdays(users):
    date_today = datetime.today().date()
    birthdays = []
    for user in users:
        birth_date = user["birthday"]
        birth_date = str(date_today.year) + birth_date[4:]
        birth_date = datetime.strptime(birth_date, "%Y.%m.%d").date()
        week_day = birth_date.isoweekday()
        days_between = (birth_date - date_today).days
        if 0 <= days_between < 7:
            if week_day < 6:
                birthdays.append(
                    {'name': user['name'], 'birthday': birth_date.strftime("%Y.%m.%d")})

            else:
                birthdays.append({'name': user['name'], 'birthday': (
                    birth_date + timedelta(days=8 - week_day)).strftime("%Y.%m.%d")})

    return birthdays


print(get_upcoming_birthdays(users))

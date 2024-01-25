# #Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами,
# що випали випадковим чином і в певному діапазоні під час чергового тиражу.
# Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо
# Вам необхідно написати функцію get_numbers_ticket(min, max, quantity),
# яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.

import random


def get_numbers_ticket(min:int, max:int, quantity:int):
    lottery_numbers = []
    if min >= 1 and max <= 1000:
        lottery_numbers = random.sample(range(min, max), quantity)
        lottery_numbers.sort()
        return lottery_numbers

    else:
        print('Значення min та max повинні бути в діапазоні від 1 до 1000') 
        return []  
       
print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 1001, 6))




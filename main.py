"""CASE 1"""

from datetime import datetime

def get_days_from_today(date):
    #   The function calculates the number of days between the specified date and the current date
    #   Input: 
    #   param date: a string representing a date in the format 'YYYY-MM-DD'
    #   Output:
    #   The function returns an integer that indicates the number of days from the specified date to the current date
      while True:
            user_date = input('enter your date in the following format "YYYY-MM-DD":  ') 
            #user enters a date in the specified format

            try: #the function performs the calculation if the date format is met
                  date = datetime.strptime(user_date, "%Y-%m-%d")
                  current_date = datetime.today()
                  date_interval = current_date - date
                  break
            
            except ValueError: #user receives a corresponding message if the date is entered in an invalid format
                  print(f'{user_date} has incorrect format. Please enter your date using the following format "YYYY-MM-DD"')
                  break

      return date_interval.days
          
result = get_days_from_today("2021-10-09")
print(result)

"""CASE 2"""
from random import randint, sample

def get_numbers_ticket(min: int, max: int, quantity: int):
    
    """The function generates and returns a sorted list of unique integer numbers in the specified range (from min to max).
    
    Input:
    param min: integer, >= 1
    param max: integer, <= 1000
    param quantity: integer, min < quantity < max

    Output:
    A sorted list of unique integer numbers in the specified range
    """

    if min >= 1 and max <= 1000 and min < quantity < max:
        numbers_tickets = sorted(sample(range(min, max), quantity))
        return numbers_tickets
    #if the conditions for all parameters are met, the function returns the required list"""
    
    else:
        print("Check your input conditions")
    
    #if the condition for at least one parameter is not met, the user receives a corresponding message"""

lottery_numbers = get_numbers_ticket(1, 50, 15)
print("Your lottery numbers are:", lottery_numbers)

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
]

def normalize_phone(phone_number):
    """Функція нормалізує телефонні номери до стандартного формату, залишаючи тільки цифри та символ '+' на початку
    Input:
    param phone_number - це рядок з телефонним номером у різноманітних форматах
    Output:
    Функція повертає нормалізований телефонний номер у вигляді рядка
    
    
    """
    for num in raw_numbers:
        normalize_phone = re.sub(r'\D', '', num) #код видаляє пробіли та інші від літери символи
        if not normalize_phone.startswith('+'): #код виконує дії, якщо номер телефону не починається з "+"
            if normalize_phone.startswith('380'):
                normalize_phone = "+" + normalize_phone #код додає "+", якщо номер починається на "380"
            else:
                normalize_phone = "+38" + normalize_phone #код додає "+380" до очищеного номеру
        return normalize_phone            


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
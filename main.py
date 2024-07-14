"""CASE 1"""

from datetime import datetime

def get_days_from_today(date):
    #   The function calculates the number of days between the specified date and the current date
    #   Input: 
    #   param date: a string representing a date in the format 'YYYY-MM-DD'
    #   Output:
    #   The function returns an integer that indicates the number of days from the specified date to the current date
      

    try: #the function performs the calculation if the date format is met
        date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today()
        date_interval = current_date - date
                
    except ValueError: #user receives a corresponding message if the date is entered in an invalid format
        print(f'{date} has incorrect format. Please enter your date using the following format "YYYY-MM-DD"')
    
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

    if min >= 1 and max <= 1000 and min < max and quantity <= (max-min):
        numbers_tickets = sorted(sample(range(min, max), quantity))
        return numbers_tickets
    #if the conditions for all parameters are met, the function returns the required list"""
    
    else:
        numbers_tickets = list()
        return numbers_tickets 
    
    #if the condition for at least one parameter is not met, the function returns an empty list"""

lottery_numbers = get_numbers_ticket(16, 15, 5)
print("Your lottery numbers are:", lottery_numbers)


"""CASE 3"""

import re

def normalize_phone(phone_number):
    # """Функція нормалізує телефонні номери до стандартного формату, залишаючи тільки цифри та символ '+' на початку
    # Input:
    # param phone_number - це рядок з телефонним номером у різноманітних форматах
    # Output:
    # Функція повертає нормалізований телефонний номер у вигляді рядка
    #"""
  
    normalize_phone = re.sub(r'\D', '', phone_number) #код видаляє пробіли та інші від літери символи
    if not normalize_phone.startswith('+'): #код виконує дії, якщо номер телефону не починається з "+"
        if normalize_phone.startswith('380'):
            normalize_phone = "+" + normalize_phone #код додає "+", якщо номер починається на "380"
        else:
            normalize_phone = "+38" + normalize_phone #код додає "+380" до очищеного номеру
    return normalize_phone            

sanitized_number = normalize_phone("38050 111 22 11   ") 
print("Нормалізований номер телефону для SMS-розсилки:", sanitized_number)
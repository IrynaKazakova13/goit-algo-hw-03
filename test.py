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

sanitized_number = normalize_phone("38050-111-22-22") 
print("Нормалізований номер телефону для SMS-розсилки:", sanitized_number)
""" Написать функцию check_login, которая будет принимать строку и проверять, что она является логином, который соответствует следующим правилам:
Длина от 5 до 20 символов
Состоит из букв верхнего и нижнего регистра, цифр, знаков подчеркивания
"""
import re
def check_login(login: str):
    if len(login) > 5 or len(login) < 20:
        return True

    if re.match(r'^[a-zA-Z0-9_]+$', login):
        return True
    else:
        return False


login_1 = "8889dnfjfvn"
print(check_login(login_1))

print("_______________________________________________________________________________________________________________")
"""Написать функцию check_phone, которая будет принимать строку и проверять,что она соответствует шаблону:
1. код страны +375
2. код оператора 29, 33, 44, 25 в скобках
3. три цифры
4. тире
5. две цифры
6. тире
7 две цифры"""

def check_phone(phone_number):
    pattern = r'^\+375 \((29|33|44|25)\) \d{3}-\d{2}-\d{2}$'

    if re.match(pattern, phone_number):
        return True
    else:
        return False

phone = "+375 (29) 534-74-66"
print(check_phone(phone))



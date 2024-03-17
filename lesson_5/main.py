# В семье свадьба. Они решили выбрать заведение, где будут праздновать взависимости от количества людей, которое прибудет к утру.
# Если их будет больше 50 - закажут ресторан.
# Eсли от 20 до 50 -то кафе.
# Если меньше 20 то отпраздную дома.
# Вывести "ресторан", "кафе", "дом" в зависимости от количества гостей.

guest = int(input('number of guests:'))
if guest > 50:
    print('Restaurant')
elif 49 >= guest >= 21:
    print('Cafe')
elif guest <= 20:
    print('Home')

# Ввести строку.
# Если длина строки больше 10 символов, то создать новую строку с 3 восклицательными знаками в конце ('!!!') и вывести на экран.
# Если меньше 10, то вывести на экран второй символ строки.

string = input("Введите строку: ")
if len(string) >= 10:
    new_string = string + "!!!"
   print(new_string)
if len(string) < 9:
    print (string[1])

# Получить на ввод количество рублей и копеек и вывести в правильной форме: например, 3 рубля, 1 рубль 25 копеек, 3 копейки.
# До 10р *
# До 100р **
# До 1000р ***

rubles = int(input("Введите количество рублей: "))
penny = int(input("Введите количество копеек: "))
if rubles < 10:
    if rubles == 1:
        rubles_str = "1 рубль"
    else:
        rubles_str = str(rubles) + " рубля"
    if penny == 1:
        penny = "1 копейка"
    else:
        penny_str = str(penny) + " копейки"

    if rubles > 0 and penny > 0:
        print(rubles_str + ", " + penny_str)
    elif rubles > 0:
        print(rubles_str)
    elif penny > 0:
        print(penny_str)
else:
    print("Введите сумму до 10 рублей.")
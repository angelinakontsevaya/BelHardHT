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


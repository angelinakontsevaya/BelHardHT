# 1.
# Создать два списка произвольного содержания.
# Добавить к каждому списку по одному элементу в конец и в начало.
# Расширить первый список вторым.
# Все изменения выводить на экран.
list_1 = [1, 2, 3, 4]
list_2 = ['spring', 'summer', 'autumn']
print(list_1, list_2)
list_1.append(5)
list_2.append('winter')
print(list_1, list_2)
list_1.insert(0, 0)
list_2.insert(0, 'winter')
print(list_1, list_2)
list_1.extend(list_2)
print(list_1, list_2)

# Создать два списка, с одинаковым кол-вом элементов. Сделать из этих списков словарь.
list_3 = [1, 2]
list_4 = ['a', 'b']
dict_first = dict([list_3, list_4])
print(dict_first)

# Работа с Дзен Python
# Количество строк: Определите количество строк в Дзене Питона.
# Ключевые слова: Подсчитайте количество вхождений ключевых cлов из Дзена Питона, таких как "is", "and", "or".
# cложить в словарь такого типа {“is”: 4, “and”: None, “or”: 100}
# Замена словa: Замените все вхождения слова "is" в Дзене Питона на "is nothing

dzen_of_python = """ Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

lines = dzen_of_python.split("\n")
num_lines = len(lines)
print(num_lines)

keywords = ["is", "and", "or"]
keyword_counts = {keyword: dzen_of_python.count(keyword) for keyword in keywords}
print(keyword_counts)

print(dzen_of_python.replace('is','is nothing'))

















































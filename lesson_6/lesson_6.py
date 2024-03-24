def bel(number):
    if number <= 10:
        return number + 5
    else:
        return number - 3
print(bel(11))
print('-----------------------------------------')
def reverse_string(input_string):
    return input_string[::-1]
print(reverse_string("Hello,Angelina!"))
print('-----------------------------------------')

animal = {'name': 'pig', 'count': 1}
def plus(a):
      animal['count'] += a
def minus(b):
    animal['count'] -= b
def change(new_name,new_count):
    animal['name'] = new_name
    animal['count'] = new_count
change('dog', 5)
print(animal)
print('-----------------------------------------')

lambda_filter = list(filter(lambda x: len(x)>5,['Angelina','Alex','Olga']))
print(lambda_filter)
print('-----------------------------------------')
def func(a):
    def func2(b):
        return f"Первая переменная - {a}, a это вторая - {b}"
    return func2

word_1 = func("python")
result = word_1("python 3")

print(result)
print('-----------------------------------------')

def user(name,age,company="Pyth", experience = 1):
    return {
        "name": name,
        "age": age,
        "company": company,
        "experience": experience,
    }

print(user(name="Angelina", age= 26, company="Asstra", experience= 5 ))
print(user(name="Angelina", age= 26))
print('-----------------------------------------')

global_var = 123

def some_function():
    local_var = 321
    print(globals())
    print(locals())

print("-----------------------------------------")






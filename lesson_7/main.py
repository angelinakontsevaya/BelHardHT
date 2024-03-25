"""Task 1
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты."""

class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f"{self.name} is jumping!")
    def run(self):
        print(f"{self.name} is running!")
    def bark(self):
        print(f"{self.name} is barking!")

    """Taks 2
    Добавить в класс Dog метод change_name. 
    Метод принимает на вход новое имя и меняет атрибут имени у объекта.
    Создать один объект класса. Вывести имя.
    Вызвать метод change_name. Вывести имя."""
    def change_name(self, new_name):
        self.name = new_name

my_dog = Dog(height=25, weight=5, name="Unik", age=1)

my_dog.jump()
my_dog.run()
my_dog.bark()

print(my_dog.height)
print(my_dog.weight)
print(my_dog.name)
print(my_dog.age)

print(f"Initial Name: {my_dog.name}")
my_dog.change_name("Alex")
print(f"Updated Name: {my_dog.name}")

"""Task 3
Создать класс Phone, у которого будут следующие атрибуты, определить атрибуты:
- brand - бренд
- model - модель
- issue_year - год выпуска
  Определить методы:
- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
  Бренд: {}
  Модель: {}
  Год выпуска: {}"""

class Phone:
    brand: str
    model: str
    issue_year: int

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, caller_name):
        print(f"Звонит {caller_name}")

    def get_info(self):
        return(self.brand, self.model, self.issue_year)

    def __str__(self):
        return f"Бренд:{self.brand}, Модель:{self.model}, Год выпуска:{self.issue_year}"


my_phone = Phone("Apple", "iPhone 14pro", 2023)

my_phone.receive_call("Alex")

phone_info = my_phone.get_info()
print(phone_info)

phone_str = my_phone.__str__()
print(phone_str)

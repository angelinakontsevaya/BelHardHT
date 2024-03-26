class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def voice(self):
        print('Подать голос')

class Dog(Animal):
    pass

dog = Dog("Unik",8)
dog.voice()
print("-------------------------------------------------------------------------------------")

class Bird(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fly(self):
        print("Я не ЮГ")

bird = Bird("Ang", 3)
bird.fly()
print("------------------------------------------------------------------------------------")

class Insect(Dog,Bird):

    def fly(self):
        print("Я не лечу на ЮГ")

    def jump(self):
        print("Я прыгаю")
insect = Insect("O",4)
insect.fly()
insect.voice()
print("---------------------------------------------------------------------------------------------------")

dog.voice()
bird.voice()
insect.voice()

insect.jump()
print("____________________________________________________________________________________________________")

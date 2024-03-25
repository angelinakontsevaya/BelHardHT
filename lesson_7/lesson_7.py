class Animal:
    title_zoo = "Zoo"
    animal_type_count = 100
    animal_type: str

    @classmethod
    def count(cls):
        return cls.animal_type_count + 1


    def __init__(self, animal_type):
        self.animal_type = animal_type

animal_1 = Animal('Cat')
print(animal_1.animal_type)
print(animal_1.title_zoo)

print(Animal.count( ))


class Calculator:

    def sum(self,num, num_2):
        return num + num_2

    def minus(self, num, num_2):
        return num - num_2

    def multiply(self, num, num_2):
        return num * num_2

    def delete(self, num, num_2):
        if num_2 != 0:
            return num / num_2

calc = Calculator()
calc_sum = calc.sum(2,5)
print(calc_sum)


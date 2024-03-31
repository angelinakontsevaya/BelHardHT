class BookCard:
    def __init__(self, author, title, year):
        self.__author = author
        self.__title = title
        self.__year = year

    def __lt__(self, other):
        return self.__year < other.__year

    def __le__(self, other):
        return self.__year <= other.__year

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year

    def __gt__(self, other):
        return self.__year > other.__year

    def __ge__(self, other):
        return self.__year >= other.__year

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise ValueError("Автор должен быть строкой")
        self.__author = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Название книги должно быть строкой")
        self.__title = value

new = BookCard(6, 56, 1234)

print("_______________________________________________________________________________________________________________")
class AmericanPerson:
    def i_love_science(self):
        return "I love science"

class RussianPerson:
    def i_love_science(self):
        return "Я люблю науку"

class GermanyPerson:
    def  i_love_science(self):
        return "ich liebe Wissenschaft"

def person_love_science(person):
    return  f"{person.__class__.__name__} says that: {person.i_love_science()}"

if __name__ == "__main__":
    american = AmericanPerson()
    russian = RussianPerson()
    german = GermanyPerson()

print(person_love_science(american))
print(person_love_science(russian))
print(person_love_science(german))

print("_______________________________________________________________________________________________________________")

from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, brand, model, issue_year, color):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.color = color
        self.mileage = 0
    @abstractmethod
    def move(self, num_km):
        if num_km <= 0:
            raise ValueError("Расстояние должно быть положительным числом")
        self.mileage += num_km

class Car(Transport):
    def __init__(self,brand, model, issue_year, color, engine_type):
         super().__init__(brand, model, issue_year, color)
         self.engine_type = engine_type
    def move(self, num_km):
        super().move(num_km)
        return f"{self.brand} {self.model} ({self.color} - {self.issue_year}) проехала {num_km} километров"

class Airplane(Transport):
    def __init__(self, brand, model, issue_year, color, lifting_capacity):
        super().__init__(brand, model, issue_year, color)
        self.lifting_capacity = lifting_capacity

    def move(self, num_km):
        super().move(num_km)
        return f'"{self.brand} {self.model} ({self.color} - {self.issue_year}) пролетел {num_km}километров'












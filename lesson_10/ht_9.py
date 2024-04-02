
"""Написать pydantic модели:
Для добавления объекта(все поля)
Для получения всех объектов(только id и name)
Для получения определенного объекта(все поля)"""

from typing import Optional, List
from pydantic import BaseModel
import json

#Для добавления объекта(все поля)
class User(BaseModel):
 id: int
 name: str
 age: int
 interests: Optional[List[str]] = []
 salary: float

#Для получения всех объектов(только id и name)
class UserInput(BaseModel):
 id: int
 name: str

#Для получения определенного объекта(все поля)
class UserObj(User):
 pass

"""Написать 3 метода(функции):
Добавление объекта в файл
Получения всех объектов
Получение определенного объекта"""

#Добавление объекта в файл

def add_user_to_file(user: UserInput):
 with open("data.json", "r") as file:
  data = json.load(file)






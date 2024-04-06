"""Написать pydantic модели:
Для добавления объекта(все поля)
Для получения всех объектов(только id и name)
Для получения определенного объекта(все поля)"""

from typing import Optional, List
from pydantic import BaseModel

#Для добавления объекта(все поля)
class Object(BaseModel):
 id: int
 name: str
 age: int
 interests: Optional[List[str]] = []
 salary: float

#Для получения всех объектов(только id и name)
class Object_get_all(Object):
 id: int
 name: str

#Для получения определенного объекта(все поля)
class Object_get(Object):
 pass

"""Написать 3 метода(функции):
Добавление объекта в файл
Получения всех объектов
Получение определенного объекта"""

import json

#Добавление объекта в файл
def read_data_from_file(file_path):
 with open(file_path, "r") as file:
  data = json.load(file)
  return data







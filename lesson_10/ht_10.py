from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: int
    name: str
    age: int
    interests: Optional[List[str]]
    salary: float
class UserInput(BaseModel):
    name: str
    age: int
    interests: Optional[List[str]]
    salary: float

class UserOutput(BaseModel):
    id: int
    name: str
import json

def add_user_to_file(user: UserInput):
    with open('data.json', 'r') as file:
        data = json.load(file)

    new_id = max([obj['id'] for obj in data]) + 1

    new_user = {
        'id': new_id,
        'name': user.name,
        'age': user.age,
        'interests': user.interests,
        'salary': user.salary
    }

    data.append(new_user)

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def get_all_users():
    with open('data.json', 'r') as file:
        data = json.load(file)

    return [UserOutput(id=obj['id'], name=obj['name']) for obj in data]

def get_user_by_id(user_id: int):
    with open('data.json', 'r') as file:
        data = json.load(file)

    user = next((obj for obj in data if obj['id'] == user_id), None)

    if user:
        return User(**user)
    else:
        return None
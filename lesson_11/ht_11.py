import pymongo

# Подключение к MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Cars"]
collection = db["cars_collection"]

# Добавление 10 машин
cars_data = [
    {"Марка": "Audi", "Модель": "A4", "Пробег": 50000, "Стоимость": 25000},
    {"Марка": "BMW", "Модель": "X5", "Пробег": 60000, "Стоимость": 30000},
    {"Марка": "Mercedes-Benz", "Модель": "E-Class", "Пробег": 45000, "Стоимость": 28000},
    {"Марка": "Toyota", "Модель": "Corolla", "Пробег": 40000, "Стоимость": 20000},
    {"Марка": "Honda", "Модель": "Civic", "Пробег": 35000, "Стоимость": 18000},
    {"Марка": "Ford", "Модель": "Focus", "Пробег": 30000, "Стоимость": 15000},
    {"Марка": "Chevrolet", "Модель": "Camaro", "Пробег": 70000, "Стоимость": 35000},
    {"Марка": "Volkswagen", "Модель": "Golf", "Пробег": 32000, "Стоимость": 16000},
    {"Марка": "Hyundai", "Модель": "Elantra", "Пробег": 28000, "Стоимость": 14000},
    {"Марка": "Kia", "Модель": "Optima", "Пробег": 26000, "Стоимость": 13000}
]
collection.insert_many(cars_data)
# Фильтр-запросы
most_expensive_car = collection.find_one(sort=[("Стоимость", pymongo.DESCENDING)])
cheapest_car = collection.find_one(sort=[("Стоимость", pymongo.ASCENDING)])
sorted_by_mileage = collection.find().sort("Пробег")
min_mileage_cars = collection.find().sort("Пробег").limit(3)

print("Самая дорогая машина:")
print(most_expensive_car)
print("\nСамая дешевая машина:")
print(cheapest_car)
print("\nОтсортированы по пробегу от меньшего к большему:")
for car in sorted_by_mileage:
    print(car)
print("\nВывести 3 авто с минимальными пробегами:")
for car in min_mileage_cars:
    print(car)gig
class CarClass:
    door: str

    def __init__(self, door):
        self.door = door

car_1 = CarClass("qwe")
print(car_1.door)
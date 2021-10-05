class Car:
    def __init__(self, mileage: int, color: str) -> None:
        self.mileage = mileage
        self.color = color
        pass


blueCar = Car(20000, "blue")
redCar = Car(30000, "red")

print(f"The blue car has {blueCar.mileage} miles")
print(f"The red car has {redCar.mileage} miles")

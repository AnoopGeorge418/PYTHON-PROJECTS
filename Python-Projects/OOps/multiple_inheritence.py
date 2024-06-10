class FlyingVehicle:
    def fly(self):
        print("Flying")

class Car:
    def drive(self):
        print("Driving")

class FlyingCar(FlyingVehicle, Car):
    pass

flying_car = FlyingCar()
flying_car.fly()
flying_car.drive()

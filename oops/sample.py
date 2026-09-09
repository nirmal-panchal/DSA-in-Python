class Car:
    total_cars = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1
        
    
    # encapsulate the brand variable
    def get_brand(self):
        return self.__brand + "!"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_desc():
        return "Cars are use for transport"    
        
    def full_name(self):
        return f"{self.__brand} {self.__model}"

    @property
    def model(self):
        return self.__model


# Inheritence
class ElectriCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
                return "Electric Charge"

my_car = Car("Tata", "Manza")
# print(my_car.brand)
# print(my_car.fuel_type())
# print(my_car.full_name())

my_electric_car = ElectriCar("Tata", "Punch", "40 KWh")
# print(my_electric_car.get_brand())
# print(my_electric_car.fuel_type())
# print(my_electric_car.model)
# print(my_electric_car.battery_size)
# print(my_electric_car.full_name())
# print(Car.total_cars)
# print(Car.general_desc())

print(isinstance(my_car, ElectriCar))
print(isinstance(my_electric_car, Car))
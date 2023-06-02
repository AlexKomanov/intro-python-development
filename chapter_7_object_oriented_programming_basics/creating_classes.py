from tire import Tire, SnowTire


class Car:
    """
    Car models a car with tires and an engine
    """

    def __init__(self, engine, tires):
        """
        Init function of the class
        """
        self.engine = engine
        self.tires = tires

    def description(self):
        print(f"A car with an {self.engine} engine, and {self.tires} tires.")


my_car = Car('electrical', [25, 25, 25, 25])


print(my_car)
print(my_car.tires)
print(my_car.engine)
my_car.license = 'B'
print(my_car.license)

my_car.description()

tire = Tire('P', 205, 55, 16, "TOYO")
snow_tire = SnowTire('P', 205, 55, 16, 25,  "GL")
tires = [tire, tire, tire, tire]
snow_tires = [snow_tire, snow_tire, snow_tire, snow_tire]

my_car2 = Car('electrical', tires=tires)
my_car3 = Car('electrical', tires=snow_tires)

my_car2.description()
my_car3.description()


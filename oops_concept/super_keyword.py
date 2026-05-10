"""
super keyword: super() generally super method we can use to access the parent class methods, constructors.

"""
class vehicle:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        print(self.name, self.year)

    def get_vehicle_name(self):
        print(self.name)

# obj = vehicle("Nageswari")


class HarlyDavidSon(vehicle):
    def __init__(self, colour, name, year):
        self.colour = colour
        print(self.colour)
        super().__init__(name, year)

    def get_vehicle_name(self):
        super().get_vehicle_name()

obj = HarlyDavidSon("Red", "Harly", 2025)
obj.get_vehicle_name()



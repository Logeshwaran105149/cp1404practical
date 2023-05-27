"""CP1404/CP5632 Practical - Car class example."""


class Car:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def drive(self, distance):
        """Drive like the wind, up to the distance provided."""
        if distance > self.fuel:
            distance = self.fuel  # Can't drive beyond available fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance

        return distance

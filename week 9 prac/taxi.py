from Car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, price_per_km=1.23):
        super().__init__(name, fuel)
        self.price_per_km = price_per_km
        self.current_fare_distance = 0

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}, {self.odometer}km on current fare, ${self.price_per_km}/km "

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

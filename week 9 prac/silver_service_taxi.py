from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel, 1.23 * fanciness)
        self.fanciness = fanciness

    def get_fare(self):
        """Return the price for the taxi trip including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}, {self.odometer}km on current " \
               f"fare, ${self.price_per_km}/km plus flagfall of ${self.flagfall:.2f} "


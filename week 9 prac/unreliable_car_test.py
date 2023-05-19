from unreliable_car import UnreliableCar

# Create a new UnreliableCar object
my_car = UnreliableCar("My Car", 100, 50)

# Attempt to drive the car 40 km
distance = my_car.drive(40)
print(f"My car drove {distance}km")

# Attempt to drive the car another 60 km
distance = my_car.drive(60)
print(f"My car drove {distance}km")

# Print the car's details
print(my_car)

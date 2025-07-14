"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Sedan", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # Create a new Car object called "limo" with 100 units of fuel
    limo = Car("Limo", 100)

    # Add 20 more units of fuel to limo
    limo.add_fuel(20)

    # Print the amount of fuel in limo
    print(f"Limo has fuel: {limo.fuel}")

    # Attempt to drive limo 115 km
    distance_driven = limo.drive(115)
    print(f"Limo drove {distance_driven}km")

    # Print car objects to verify __str__ method
    print(my_car)
    print(limo)


main()

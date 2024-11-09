"""
Author: Catelynn Barfell
Date written: 11/07/24
Assignment: Module 3 Lab - Case Study: Lists, Functions, and Classes
Short Desc: A Python app to create and display vehicle information using inheritance with Vehicle and Automobile classes.
"""

# Initializes the Vehicle class with a vehicle type attribute
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Initializes the Automobile class with year, make, model, doors, and roof attributes.
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Function to gather input from the user
def get_user_input():
    print("Please enter the details for your car.")
    vehicle_type = "car"
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    while True:
        try:
            doors = int(input("Number of doors (2 or 4): "))
            if doors in [2, 4]:
                break
            else:
                print("Invalid input. Please enter 2 or 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    roof = input("Type of roof (solid or sun roof): ").lower()
    while roof not in ["solid", "sun roof"]:
        print("Invalid input. Please enter 'solid' or 'sun roof'.")
        roof = input("Type of roof (solid or sun roof): ").lower()
    
    return Automobile(vehicle_type, year, make, model, doors, roof)

# Function to display the car details
def display_car_details(car):
    print("\nHere are the details of your car:")
    print(f"  Vehicle type: {car.vehicle_type}")
    print(f"  Year: {car.year}")
    print(f"  Make: {car.make}")
    print(f"  Model: {car.model}")
    print(f"  Number of doors: {car.doors}")
    print(f"  Type of roof: {car.roof}")

# Main program
def main():
    car = get_user_input()
    display_car_details(car)

if __name__ == "__main__":
    main()
# simple equality if statement
cars = ["audi", "bmw", "lada", "ferailery"]
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# inequality
requested_toppings = ['cheese', "pepperoni", 'capsicum']
for topping in requested_toppings:
    if topping != "pinaple":
        print("Pizza is saved no pinaples is found")
    else:
        print("Your pizza came from hell eat your fucking pinaple")
def fuel_calculator():
    kilometers = int(input("Enter the kilometers you will drive: "))
    fuel = float(input("Enter the  current price per liter of fuel: "))

    liters_needed = kilometers / 10
    fuel_needed = liters_needed * fuel

    print(round(fuel_needed, 2))

fuel_calculator()
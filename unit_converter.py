def unit_converter():
    try:
        value = float(input("Enter the value: "))
    except ValueError:
        print("Enter a valid number!")
        return

    from_unit = input("Enter the unit (Km/Miles) or (C/F): ").lower()
    to_unit = input("Enter the unit you want to change (Km/Miles) or (C/F): ").lower()

    if from_unit == "km" and to_unit == "miles":
        print(f"{value}Km = {value*0.621371}Miles")
    elif from_unit == "miles" and to_unit == "km":
        print(f"{value}Miles = {value/0.621371}Km")
    elif from_unit == "c" and to_unit == "f":
        print(f"{value}°C = {(value*(9/5))+32}°F")
    elif from_unit == "f" and to_unit == "c":
        print(f"{value}°F = {(value-32)*5/9}°C")
    else:
        print("Invalid Unit!")


unit_converter()

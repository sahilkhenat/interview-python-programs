"""Write a program to convert units.
Convert Distance: Convert kilometers to miles.
Convert Temperature: Convert Celsius temperature to Fahrenheit.
"""


def convert_distance(from_unit, to_unit, quantity):
    if from_unit == 'kms' and to_unit == 'miles':
        return convert_km_to_miles(quantity)
    elif from_unit == 'miles' and to_unit == 'kms':
        return convert_miles_to_km(quantity)


def convert_temperature(from_unit, to_unit, quantity):
    if from_unit == 'C' and to_unit == 'F':
        return convert_celsius_to_fahrenheit(quantity)
    elif from_unit == 'F' and to_unit == 'C':
        return convert_fahrenheit_to_celsius(quantity)


def convert_km_to_miles(distance):
    return distance * 0.621371


def convert_miles_to_km(distance):
    return distance * 1.60934


def convert_celsius_to_fahrenheit(temperature):
    return (temperature * 9 / 5) + 32


def convert_fahrenheit_to_celsius(temperature):
    return (temperature - 32) * 5 / 9


def main():
    from_unit =''
    to_unit = ''
    print("\n1. Distance\n2. Temperature")
    property_type = int(input("Enter your choice: "))

    if property_type == 1:
        print("\n1. Kilometers to Miles\n2. Miles to Kilometers")
        conversion_choice = int(input("Enter your choice: "))

        if conversion_choice == 1:
            from_unit = 'kms'
            to_unit = 'miles'
        elif conversion_choice == 2:
            from_unit = 'miles'
            to_unit = 'kms'
        else:
            print("Invalid choice")

        quantity = float(input(f"Enter distance in {from_unit}: "))
        converted_unit = convert_distance(from_unit, to_unit, quantity)
        print(f"{quantity} {from_unit} = {converted_unit} {to_unit}")

    elif property_type == 2:
        print("\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius")
        conversion_choice = int(input("Enter your choice: "))

        if conversion_choice == 1:
            from_unit = 'C'
            to_unit = 'F'
        elif conversion_choice == 2:
            from_unit = 'F'
            to_unit = 'C'
        else:
            print("Invalid choice")

        temperature = float(input(f"Enter temperature in {from_unit} to convert to {to_unit}: "))
        converted_temperature = convert_temperature(from_unit, to_unit, temperature)
        print(f"{temperature} {from_unit} = {converted_temperature} {to_unit}")

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()

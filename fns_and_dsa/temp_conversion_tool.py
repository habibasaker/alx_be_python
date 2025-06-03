# temp_conversion_tool.py

# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Used for converting F to C
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Used for converting C to F

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Use global conversion factor to convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    # Use global conversion factor to convert Celsius to Fahrenheit
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Main logic to interact with user
def main():
    # Prompt the user to enter a temperature to convert
    temp_input = input("Enter the temperature to convert: ")

    # Try converting the input to float to validate it is numeric
    try:
        temperature = float(temp_input)
    except ValueError:
        # If the conversion fails, raise an error
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Ask the user to specify the temperature unit (C or F)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Perform conversion based on the unit
    if unit == "F":
        # Call function to convert Fahrenheit to Celsius
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")
    elif unit == "C":
        # Call function to convert Celsius to Fahrenheit
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")
    else:
        # Handle invalid unit input
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()



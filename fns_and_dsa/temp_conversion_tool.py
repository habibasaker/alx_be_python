# temp_conversion_tool.py

# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    future_celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return future_celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    future_fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return future_fahrenheit

# Prompt the user to enter a temperature
temp_input = input("Enter the temperature to convert: ")

# Validate numeric input
try:
    temperature = float(temp_input)
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")

# Ask the user for the temperature unit
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

# Perform conversion based on the unit
if unit == "F":
    future_celsius = convert_to_celsius(temperature)
    print(f"{temperature}°F is {future_celsius}°C")
elif unit == "C":
    future_fahrenheit = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {future_fahrenheit}°F")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")



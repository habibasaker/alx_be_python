# pattern_drawing.py

# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for each row
while row < size:
    # Use a for loop to print asterisks in a row
    for col in range(size):
        print("*", end="")
    # Move to the next line after a row is printed
    print()
    row += 1


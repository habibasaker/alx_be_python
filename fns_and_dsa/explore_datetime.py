
# explore_datetime.py

# Import the datetime and timedelta classes from the datetime module
from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time using datetime.now()
    current_date = datetime.now()

    # Format the current date and time in "YYYY-MM-DD HH:MM:SS" format
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Print the formatted current date and time
    print(f"Current date and time: {formatted_date}")

    # Return the current_date for use in other functions
    return current_date


# Part 2: Calculate a Future Date
def calculate_future_date(current_date):
    try:
        # Prompt the user to enter the number of days to add
        days_to_add = int(input("Enter the number of days to add to the current date: "))

        # Create a timedelta object representing the number of days
        delta = timedelta(days=days_to_add)

        # Add the timedelta to the current date to calculate the future date
        future_date = current_date + delta

        # Format and print the future date in "YYYY-MM-DD" format
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter a valid integer number of days.")

# Main program flow
if __name__ == "__main__":
    # Call the function to display current date and time and get the current date
    current = display_current_datetime()

    # Call the function to calculate and display the future date
    calculate_future_date(current)

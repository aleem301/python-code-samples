# Your Name Aleemuddin Ather Mohammed
# Date 10/09/2024
# Assignment 3

# Remember to comment for each function

def print_hello():
     # Print "Hello World"
    print("Hello World")
    # TODO: Print "Hello World"
    pass

def hello_user(name):
     # Print a greeting message with the user's name
    print(f"Hello, {name}!")
    # TODO: Print "Hello, their_name"
    pass

def get_circle_area(radius):
     # Calculate and print the area of a circle given the radius
    area = math.pi * (radius ** 2)
    print(f"The area of the circle with radius {radius} is {area:.2f}.")
    # TODO: print a message back with the answer
    pass

def get_miles_per_galoon(miles, gallons):
     # Calculate and print the MPG for the car
    if gallons == 0:  # Prevent division by zero
        print("Gallons used cannot be zero.")
    else:
        mpg = miles / gallons
        print(f"Your car's MPG is {mpg:.2f}.")
    # TODO: print out the MPG for the car
    pass
    
def convert_temperature(temperature_F):
    # Convert Fahrenheit to Celsius and return the converted temperature
    temperature_C = (temperature_F - 32) * (5 / 9)
    return temperature_C
    # TODO: return the coverted temperature in Celcius
    pass

def problem_7(starting_day, length_of_stay):
    # Calculate the day of the week when returning from a holiday
    return_day = (starting_day + length_of_stay) % 7
    print(f"You will return on day {return_day} of the week.")
    # TODO: Implement the function as the problem statement
    pass

def extra_credit_problem_1():
    start_year = 1900
    end_year = 2100
    # Print leap years from the year 1900 to 2100
    print("Leap years from 1900 to 2100:")
    for year in range(start_year, end_year + 1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(year)
    # TODO: Write a program to print leap years from the year 1900 to 2100
    # 5 points extra credits
    pass

def extra_credit_problem_2(n):
     # Check if n is a prime number
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    # a prime number is a natural number greater than 1, that can only divisible by itself and 1
    # 10 points extra credits
    # TODO: given the number n, check if n is a prime number
    pass


def main():
    print_hello()
    # prompt user to get the input then call functions
    # ...
    print_hello()  # Problem 1
    
    name = input("What is your name? ")  # Get user name for Problem 2
    hello_user(name)
    
    radius = float(input("Enter the radius of the circle: "))  # Problem 3
    get_circle_area(radius)
    
    miles = float(input("Enter the number of miles driven: "))  # Problem 4
    gallons = float(input("Enter the number of gallons used: "))
    get_miles_per_gallon(miles, gallons)
    
    temperature_F = float(input("Enter temperature in Fahrenheit: "))  # Problem 5
    temperature_C = convert_temperature(temperature_F)
    print(f"{temperature_F} degrees Fahrenheit is {temperature_C:.2f} degrees Celsius.")
    
    starting_day = int(input("Enter the starting day number (0 for Sunday, 6 for Saturday): "))  # Problem 6
    length_of_stay = int(input("Enter the length of your stay in nights: "))
    problem_7(starting_day, length_of_stay)

    extra_credit_problem_1()  # Extra Credit Problem 1

    n = int(input("Enter a number to check if it is prime (Extra Credit Problem 2): "))  # Extra Credit Problem 2
    if extra_credit_problem_2(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
    
main()


    



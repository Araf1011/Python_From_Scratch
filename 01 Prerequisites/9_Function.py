def greet(name):
    #This function takes a name as input and returns a greeting message.
    return f"Hello, {name}!"
#Using the function
name = input("Enter your name: ") #input : Araf
greeting = greet(name)
print(greeting) #output: Hello, Araf!


#Function Parameters
# Default parameters
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # Output: 9 (3^2)
print(power(3, 3))   # Output: 27 (3^3)

# Keyword arguments
def introduce(name, age, city):
    return f"{name} is {age} years old and lives in {city}"

print(introduce(age=22, city="Chittagong", name="Araf"))
# Output: Araf is 22 years old and lives in Chittagong



#Lambda Functions
# A lambda function to calculate the square of a number
# Anonymous functions
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Common use: with map, filter
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4]

# reduce: combine iterable into one value (from functools)
from functools import reduce

product = reduce(lambda acc, x: acc * x, numbers, 1)
print(product)  # Output: 120 (1*2*3*4*5)
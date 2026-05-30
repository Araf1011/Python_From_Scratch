#In Python, values are evaluated as True or False in boolean contexts.
#Falsy Values (evaluate to False):
# All of these are falsy
bool(False)      # False
bool(None)       # False
bool(0)          # False
bool(0.0)        # False
bool(0j)         # False (complex zero)
bool("")         # False (empty string)
bool([])         # False (empty list)
bool({})         # False (empty dictionary)
bool(())         # False (empty tuple)
bool(set())      # False (empty set)

#Truthy Values (evaluate to True):
# Everything else is truthy
bool(True)       # True
bool(1)          # True
bool(-1)         # True
bool(3.14)       # True
bool("hello")    # True
bool([1, 2, 3])  # True
bool({"a": 1})   # True

#Example of using truthy and falsy values in an if statement
my_list = []
if my_list:
    print("The list is not empty.")
else:
    print("The list is empty.") #output: The list is empty.
name = input("Enter your name: ")
if name:
    print(f"Hello, {name}!") #output: Hello, Araf!
else:
    print("You didn't enter a name.") #output: You didn't enter a name.

# Default value pattern
value = None
result = value or "default"  # Uses "default" if value is falsy
print(result)  # Output: default

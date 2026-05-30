#Basic if/else statement
x = int(input("Enter a number: "))
if x > 5:
    print("x is greater than 5") #output: x is greater than 5
else:
    print("x is not greater than 5")



#Comparison operators
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

print(x > y)   # True
print(x < y)   # False
print(x == y)  # False (equality)
print(x != y)  # True (not equal)
print(x >= y)  # True
print(x <= y)  # False



#Logical operators
x = int(input("Enter a number: "))
if x > 0 and x < 10:
    print("x is between 0 and 10") #output: x is between 0 and 10
elif x >= 10 and x < 20:
    print("x is between 10 and 20") #output: x is between 10 and 20
else:
    print("x is not between 0 and 20")



#Loops
#for loop

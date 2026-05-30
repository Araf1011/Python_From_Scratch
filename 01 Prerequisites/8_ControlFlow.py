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
#Iterate over a list
games = ["Valorant", "CS:GO", "GTA V", "Minecraft"]
for game in games:
    print(game) #output: Valorant, CS:GO, GTA V, Minecraft (each on a new line) 
#using range
for i in range(5):
    print(i) #output: 0, 1, 2, 3, 4 (each on a new line)
#with index
for index, game in enumerate(games):
    print(f"{index}: {game}") #output: 0: Valorant, 1: CS:GO, 2: GTA V, 3: Minecraft (each on a new line)



#while loop
count = 0
while count < 5:
    print(count) #output: 0, 1, 2, 3, 4 (each on a new line)
    count += 1



#Loop control statements
#break statement
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0, 1, 2, 3, 4

# Continue: skip iteration
for i in range(5):
    if i == 2:
        continue
    print(i)
# Output: 0, 1, 3, 4
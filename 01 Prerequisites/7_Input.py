#The input() function is to get input from the user ...
name = input("Enter your name: ") #input : Araf
print("Hello, " + name + "!") #output: Hello, Araf!

#Type Conversion with Input
age = int(input("Enter your age: ")) #input : 23
print("You are " + str(age) + " years old.") #output: You are 23 years old.

#Using input with f-strings
height = float(input("Enter your height : ")) #input : 5.00ft
print(f"Your height is {height} feet.") #output: Your height is 5.0 feet.

#Using bool with input
is_student = input("Are you a student? (yes/no): ") #input : yes
is_student_bool = is_student.lower() == "yes" #convert to boolean
print(f"Is the user a student? {is_student_bool}") #output: Is the user a student? True



#Multiple Inputs
first_name = input("Enter your first name: ") #input : Mohammad
last_name = input("Enter your last name: ") #input : Araf
full_name = first_name + " " + last_name
age = int(input("Enter your age: ")) #input : 23
country = input("Enter your country: ") #input : Bangladesh

print(f"I am {full_name}, {age} years old, from {country}.") #output: I am Mohammad Araf, 23 years old, from Bangladesh.

#get multiple inputs in one line
info = input ("Enter your  name, age, and country (separated by commas): ") #input : Mohammad, Araf, 23, Bangladesh
name,age,country = info.split(",") #split the input into parts
age = int(age) #convert age to integer
city = city.strip() #remove any extra whitespace
print(f"I am {name}, {age} years old, from {country}.") #output: I am Mohammad Araf, 23 years old, from Bangladesh.



#Handling Wrong Input
while True:
    try:
        age = int(input("Enter your age: ")) #input : 23 or Blank 
        if age > 0:
            break
        else:
            print("Age must be a positive number.")
    except ValueError:
        print("Invalid input. Please enter a valid age.")
print(f"You are {age} years old.") #output: You are 23 years old. or Invalid input. Please enter a valid age.

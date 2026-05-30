#Types of numbers in Python
#Integer
import string


my_age = 23
print("My age is:", my_age)
print("The type of my_age is:", type(my_age))

#Float
my_height = 5.0
print("My height is:", my_height)
print("The type of my_height is:", type(my_height))

#Complex
my_complex_number = 2 + 3j
print("My complex number is:", my_complex_number)
print("The type of my_complex_number is:", type(my_complex_number))


#String Concatenation
my_name1 = "Mohammad"
my_name2 = 'Araf'

full_name = my_name1 + " " + my_name2 
print("My full name is:", full_name)
print("The type of full_name is:", type(full_name))

#String Methods
text = "Hello, World!"
print("Uppercase:", text.upper()) #convert to uppercase
print("Lowercase:", text.lower()) #convert to lowercase
print("Replace 'World' with 'Python':", text.replace("World", "Python")) #string replacement
print("length of text:", len(text)) #text length


#Boolean
is_true = True
is_false = False

#boolean operations
print("is_true AND is_false:", is_true and is_false)   #logical AND
print("is_true OR is_false:", is_true or is_false)   #logical OR
print("NOT is_true:", not is_true)   #logical NOT


#Type conversion
x = "11"
print("Before conversion, x is:", x, "and its type is:", type(x))
y = int(x)  #convert string to integer
print("After conversion, y is:", y, "and its type is:", type(y))
z = float(x)  #convert string to float
print("After conversion, z is:", z, "and its type is:", type(z))
Q = complex(x)  #convert string to complex
print("After conversion, Q is:", Q, "and its type is:", type(Q))
W = str(11)  #convert integer to string
print("After conversion, W is:", W, "and its type is:", type(W))



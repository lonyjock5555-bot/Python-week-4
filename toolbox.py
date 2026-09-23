
# toolbox.py

# Function 1: Double a number
def double(number):
    return number * 2


# Function 2: Check if a student passed
def is_pass(score):
    return score >= 50


# Function 3: Greeting with a default value
def greet(name, greeting="Hello"):
    return greeting + ", " + name + "!"


# Test the functions
print(double(5))
print(double(10))

print(is_pass(75))
print(is_pass(40))

print(greet("Lony"))
print(greet("Lony", "Welcome"))
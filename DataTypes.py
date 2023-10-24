# Data type

number = 100  # int
second = 56.78  # this is a float
text = "Hello there"  # string
ispythoninteresting = True  # bool

# data types storing multiple values ina variable
cars = ["Toyota", "Nissan", "VW"]  # list are mutable: values can change
fruits = ("banana", "oranges", "apples")  # tuple are immutable: values cannot change
countries = {"Kenya", "Tanzania", "Tunisia", "Algeria"}  # sets

# dictionaries

details = {
    "firstname": "Alfonce",
    "age": 23,
    "course": "Web development",
    "nationality": "Kenya"
}


print(second)
print(text)
print(cars)
print(details["firstname"])
print(details["age"])
print(details["course"])
print(countries)

# determining the data type
print(type(text))
print(type(countries))
print(type(details))
print(type(ispythoninteresting))

# Typecasting - converting one data type to another
# converting number(100) to a decimal
print(float(number))

# converting decimal(56.78) to integer
print(int(second))


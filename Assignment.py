# Program to check whether a year is leap year or not using pre-initialized variable
Year = 2003
if Year % 4 == 0:
    print(Year, "is a leap year")
else:
    print(Year, "is not a leap year\n")

# Program to check whether a year is leap year or not by taking inputs from the user
year = int(input("Enter year to be checked: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("The year is a leap year!\n")
else:
    print("The year isn't a leap year!\n")


# A program that checks whether an alphabet letter is consonant or a vowel

def vowelOrConsonant(x):
    if(x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'
            or x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U'):
        print(x, "is a vowel")
    else:
        print(x, "is a consonant")


vowelOrConsonant('e')
vowelOrConsonant('f')



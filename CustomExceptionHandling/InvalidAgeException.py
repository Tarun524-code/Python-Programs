class InvalidAgeException(Exception):
    pass
try:
    age = int(input("Enter Age: "))
    if age<18:
        raise InvalidAgeException
    else:
        print("You can eligible to vote")
except InvalidAgeException:
    print("Age below 18, not eligible to vote")
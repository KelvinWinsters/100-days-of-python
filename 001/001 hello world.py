from datetime import date


def one():
    print("Hello World")
    user_name = input("Enter your name ")
    user_age = int(input("Enter your age"))
    print(f"Welcome {user_name}")
    print(f"You are {user_age} years old")
    print(type(user_name))
    print(user_name.isupper())  # checks if the string is in uppercase
    print(user_name.islower())
    print(user_name.upper())  # changes the string to upper case
    print(user_name.lower())
    print(user_name[3])  # prints the third character
    print(user_name[1:4])  # prints from first to third character
    print(type(user_age))


def two():
    print("*" * 7)
    one()


if __name__ == '__main__':
    two()

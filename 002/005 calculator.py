print("Calculator App")


def my_main():
    finished = False
    while not finished:
        result = 0
        menu_choice = get_operation_choice()
        n1, n2 = get_numbers_from_user()
        if menu_choice == '1':
            result = add(n1, n2)
        elif menu_choice == '2':
            result = subtract(n1, n2)
        elif menu_choice == '3':
            result = multiply(n1, n2)
        elif menu_choice == '4':
            result = divide(n1, n2)
        elif menu_choice == '5':
            result = modulo(n1, n2)
        print(f"Result: {result}")
        print('=================')
        finished = check_if_user_has_finished()
    print('Bye')


def add(x, y):
    """" Adds two numbers """
    return x + y


def subtract(x, y):
    """ Subtracts two numbers """
    return x - y


def multiply(x, y):
    """ Multiples two numbers """
    return x * y


def divide(x, y):
    """Divides two numbers"""
    return x / y


def modulo(x, y):
    """Finds the remainder"""
    return x % y


def get_operation_choice():
    global user_selection
    input_ok = False
    while not input_ok:
        print('Menu Options are:')
        print('\t1. Add')
        print('\t2. Subtract')
        print('\t3. Multiply')
        print('\t4. Divide')
        print('\t5. Modulo')
        print('-----------------')
        user_selection = input('Please make a selection: ')
        if user_selection in ('1', '2', '3', '4', '5'):
            input_ok = True
        else:
            print('Invalid Input (must be 1 - 5)')
    print('-----------------')
    return user_selection


def get_numbers_from_user():
    num1 = get_integer_input('Input the first number: ')
    num2 = get_integer_input('Input the second number: ')
    return num1, num2


def get_integer_input(message):
    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print('The input must be an integer')
        value_as_string = input(message)
    return int(value_as_string)


def check_if_user_has_finished():
    """
    Checks that the user wants to finish or not.
    Performs some verification of the input."""
    ok_to_finish = True
    user_input_accepted = False
    while not user_input_accepted:
        user_input = input('Do you want to finish (y/n): ')
        if user_input == 'y':
            user_input_accepted = True
        elif user_input == 'n':
            ok_to_finish = False
            user_input_accepted = True
        else:
            print('Response must be (y/n), please try again')
    return ok_to_finish


my_main()

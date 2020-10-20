def my_function(num1, num2):
    print("Function In")
    result = num1 / num2
    print("Function Out")


print("Starting")
try:
    print("Before Function")
    my_function(7, 0)
    print("After Function")
except ZeroDivisionError as exp:
    print(exp)
print("Done")

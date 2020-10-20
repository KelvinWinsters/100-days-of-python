def byzero(num):
    res = num / 0
    print(res)


try:
    byzero(5)
except ZeroDivisionError as exp:
    print(f"error is caused by {exp}")
except FileNotFoundError as fnfe:
    print(f" {fnfe}")
except IndexError as e:
    print(f" {e}")
except Exception as exception:
    print(f" {exception}")

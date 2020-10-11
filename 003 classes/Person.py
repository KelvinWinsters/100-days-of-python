class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ' is ' + str(self.age)

    def birthday(self):
        print(f"Happy Birthday you were {self.age}")
        self.age += 1
        print(f"You are now {self.age}")

    def calculate_pay(self, hours_worked):
        rate_of_pay = 7.50
        if self.age >= 21:
            rate_of_pay += 2.50
        return hours_worked * rate_of_pay

    def is_teenager(self):
        return self.age < 21


p1 = Person("Patrick", 26)
print(p1.is_teenager())
pay = p1.calculate_pay(160)
print(f"Pay {p1.name} {pay}")
p2 = Person("Shawn", 20)
print(p2.is_teenager())
pay = p2.calculate_pay(160)
print(f"Pay {p2.name} {pay}")
# p3 = p2
# p2 = p1

print(id(p1))
# print(id(p2))
# print(id(p3))
# print(id(p2))
print(p1)
# print(p2)
p1.birthday()
# p2.birthday()
print(f"{p1.name} is {p1.age}")
# print(f"{p2.name} is {p2.age}")

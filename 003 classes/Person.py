class Person:
    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        print("In age method")

    def get_age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) & new_age > 0 & new_age < 120:
            self._age = new_age

    def get_name(self):
        return self._name

    def __str__(self):
        return self._name + ' is ' + str(self._age)

    def birthday(self):
        print(f"Happy Birthday you were {self._age}")
        self._age += 1
        print(f"You are now {self._age}")

    def is_teenager(self):
        return self._age < 21

    @property
    def name(self):
        return self._name


class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id

    def __str__(self):
        return super().__str__() + ' id number is ' + str(self.id)

    def calculate_pay(self, hours_worked):
        rate_of_pay = 7.50
        if self._age >= 21:
            rate_of_pay += 2.50
        return hours_worked * rate_of_pay


p1 = Employee("Patrick", 26, 1234)
print(p1.is_teenager())
pay = p1.calculate_pay(160)
print(f"Pay {p1.name} {pay}")
p2 = Employee("Shawn", 20, 5678)
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

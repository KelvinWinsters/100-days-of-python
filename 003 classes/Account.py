class Account:
    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1
        print(f"Number of Account instance created: {Account.instance_count}")

    def __init__(self, account_number, name, account_type, min_balance):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.min_balance = min_balance

    def deposit(self, min_balance):
        print(f"You are depositing {min_balance}")
        self.min_balance += min_balance
        print(f"The balance now is {self.min_balance}")

    def withdraw(self, min_balance):
        print(f"You are withdrawing {min_balance}")
        self.min_balance -= min_balance
        print(f"The balance is {self.min_balance}")

    def get_balance(self):
        print(f"Current balance is {self.min_balance}")


class CurrentAccount(Account):
    def __init__(self, account_number, name, account_type, min_balance):
        super().__init__(account_number, name, account_type, min_balance)
        print("")

    def __str__(self):
        print("")

    def withdraw(self, min_balance):
        print(f"You are withdrawing {min_balance}")
        self.min_balance -= min_balance
        print(f"The balance is {self.min_balance}")


class DepositAccount(Account):
    def __init__(self, account_number, name, account_type, min_balance):
        super().__init__(account_number, name, account_type, min_balance)
        print("")


class InvestmentAccount(Account):
    def __init__(self, account_number, name, account_type, min_balance):
        super().__init__(account_number, name, account_type, min_balance)
        print("")


acc1 = Account(1234, 'kelvin', 'savings', 15000)
acc1.increment_instance_count()
acc2 = Account(1234, 'kelvin', 'savings', 15000)
acc2.increment_instance_count()
acc3 = Account(1234, 'kelvin', 'savings', 15000)
acc3.increment_instance_count()
acc1.get_balance()
acc1.deposit(10000)
acc1.withdraw(9000)

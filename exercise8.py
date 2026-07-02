class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner 
        self.balance = balance

    def deposit(self, amount: float) -> float:
        if amount<=0:
            raise ValueError ("amount cannot be negative")
        else: 
            deposited_balance= self.balance + amount 
            return deposited_balance

        # if amount <= 0, raise ValueError
        # otherwise add to balance and return new balance
account1 = BankAccount("lebron")
print(account1.deposit(100))

try:
    print(account1.deposit(-100))
except ValueError as e:
    print(e)
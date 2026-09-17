class BankAccount:
    def __init__(self, balance: int):
        self.__balance = balance


    def get_balance(self) -> int:
        return self.__balance


    def set_balance(self, balance: int) -> None:
        if balance < 0:
            print("Cannot set negative balance!")
            return

        self.__balance = balance

        
account = BankAccount(1000)
print(account.get_balance())
account.set_balance(-100)
print(account.get_balance())
account.set_balance(100)
print(account.get_balance())
account.set_balance(0)
print(account.get_balance())

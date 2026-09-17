class Account:
    def __init__(self, title: str, balance: int):
        self.title = title
        self._balance = balance

    
    def display_balance(self) -> None:
        print(f"Balance: ${self._balance}")


account = Account("John", 1000)
account.display_balance()

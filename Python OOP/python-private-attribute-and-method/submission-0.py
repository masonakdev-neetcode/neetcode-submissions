class PasswordManager:
    def __init__(self, password: str):
        self.__password = password

    def verify_password(self, password: str) -> bool:
        return password == self.__password

    
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False

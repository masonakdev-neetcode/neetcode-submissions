from typing import Tuple

def create_pair(name: str, age: int) -> Tuple[str, int]:
    return (name, age)


print(create_pair("Alice", 25))
print(create_pair("Bob", 30))
print(create_pair("Charlie", 35))

def divide_numbers(a: str, b: str) -> None:
    try:
        print(int(a) / int(b))
    except ValueError as ignored:
        print("Error: Invalid value!")
    except ZeroDivisionError as ignored:
        print("Error: Division by zero!")
    except Exception as e:
        print("An error occurred:", e)


divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
